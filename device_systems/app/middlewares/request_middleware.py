import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 1. Obtener o generar un ID único para la petición (Correlation ID)
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4())[:8])
        
        # 2. Registrar el tiempo de inicio
        start_time = time.time()
        
        # 3. Continuar con la ejecución de la ruta
        response = await call_next(request)
        
        # 4. Calcular el tiempo total de proceso
        process_time = time.time() - start_time
        
        # 5. Agregar las cabeceras personalizadas a la respuesta
        response.headers["X-Process-Time"] = f"{process_time:.4f}"
        response.headers["X-App-Name"] = "device_systems"
        response.headers["X-Request-ID"] = request_id
        
        # 6. Registrar en consola los datos de la petición (Trazabilidad)
        print(f"[{request_id}] Method: {request.method} | Path: {request.url.path} | Status: {response.status_code} | Time: {process_time:.4f}s")
        
        return response