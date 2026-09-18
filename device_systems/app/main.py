from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.request_middleware import RequestMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.utils.limiter import limiter

# Importar los routers de tu aplicación
from app.auth.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router

app = FastAPI(
    title="device_systems API",
    description="API REST segura para gestión de usuarios, dispositivos y préstamos",
    version="3.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Operaciones de autenticación y login con OAuth2."},
        {"name": "Users", "description": "Gestión y consulta de usuarios del sistema."},
        {"name": "Devices", "description": "Administración de dispositivos (Requiere roles)."},
        {"name": "Loans", "description": "Control y gestión de préstamos de dispositivos."},
    ]
)

# Configuración de Rate Limiting y Middleware
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded, 
    lambda request, exc: _rate_limit_exceeded_handler(request, exc) # type: ignore
)

app.add_middleware(RequestMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- REGISTRAR LOS ROUTERS AQUÍ ---
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)