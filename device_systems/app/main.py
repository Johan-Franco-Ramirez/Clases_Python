from fastapi import FastAPI
from app.routes import user_routes

# Inicializar la aplicación principal de FastAPI
app = FastAPI(
    title="device_systems API",
    description="API REST para la gestión de usuarios del sistema device_systems.",
    version="1.0.0"
)

# Conectar el enrutador de usuarios
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    # Ruta raíz informativa
    return {
        "mensaje": "Bienvenido a device_systems API",
        "documentacion": "/docs"
    }