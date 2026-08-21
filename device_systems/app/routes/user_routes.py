from typing_extensions import Literal

from fastapi import APIRouter, HTTPException, status, Response
from typing import List, Optional
from app.schemas.user_schema import UserCreate, UserResponse

# Creamos el enrutador para agrupar los endpoints de usuarios
router = APIRouter(prefix="/users", tags=["Users"])

# Base de datos simulada en memoria
fake_users_db = [
    {"id": 1, "name": "Ana Gómez", "email": "ana@example.com", "role": "admin", "is_active": True},
    {"id": 2, "name": "Carlos Pérez", "email": "carlos@example.com", "role": "support", "is_active": False},
    {"id": 3, "name": "Lucía Torres", "email": "lucia@example.com", "role": "user", "is_active": True}
]

# 1. GET: Listar todos o filtrar por rol y estado (Query Parameters) + Cabeceras HTTP
@router.get("/", response_model=List[UserResponse])
def get_users(
    response: Response,
    role: Optional[Literal["admin", "support", "user"]] = None,
    is_active: Optional[bool] = None
):
    # Agregamos las cabeceras HTTP personalizadas (Fase 5)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    users = fake_users_db

    # Filtrar por rol si se envía en la URL
    if role:
        users = [u for u in users if u["role"] == role]
    
    # Filtrar por estado si se envía en la URL
    if is_active is not None:
        users = [u for u in users if u["is_active"] == is_active]

    return users

# 2. GET: Buscar usuario por ID (Path Parameter)
@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, response: Response):
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Buscar usuario en la lista
    user = next((u for u in fake_users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El usuario con ID {user_id} no existe."
        )
    return user

# 3. POST: Crear un nuevo usuario (Validación Pydantic + Correos duplicados)
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, response: Response):
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Evitar correos duplicados
    for existing_user in fake_users_db:
        if existing_user["email"] == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya se encuentra registrado."
            )

    # Generar ID automático
    new_id = max([u["id"] for u in fake_users_db], default=0) + 1

    # Construir nuevo usuario
    new_user = {
        "id": new_id,
        "name": user_data.name,
        "email": user_data.email,
        "role": user_data.role,
        "is_active": user_data.is_active
    }

    fake_users_db.append(new_user)
    return new_user