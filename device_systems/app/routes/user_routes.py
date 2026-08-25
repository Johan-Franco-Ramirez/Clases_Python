from typing_extensions import Literal
from fastapi import APIRouter, HTTPException, status, Response
from typing import List, Optional
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.services import user_service

# Agrupar endpoints de usuarios bajo el prefijo /users
router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserResponse])
def get_users(
    response: Response,
    role: Optional[Literal["admin", "support", "user"]] = None,
    is_active: Optional[bool] = None
):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    users = user_service.get_all_users()

    # Filtrar por rol si se especifica
    if role:
        users = [u for u in users if u["role"] == role]
        
    # Filtrar por estado activo si se especifica
    if is_active is not None:
        users = [u for u in users if u["is_active"] == is_active]

    return users


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, response: Response):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Buscar usuario por ID o lanzar error 404
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El usuario con ID {user_id} no existe."
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, response: Response):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Evitar correos duplicados consultando el servicio
    existing_users = user_service.get_all_users()
    for existing in existing_users:
        if existing["email"] == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya se encuentra registrado."
            )

    # Crear y retornar el nuevo usuario
    new_user = user_service.create_user(user_data.model_dump())
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user_complete(user_id: int, user_data: UserCreate, response: Response):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Reemplazar completamente los datos del usuario por ID
    updated_user = user_service.update_user(user_id, user_data.model_dump())
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El usuario con ID {user_id} no existe."
        )
    return updated_user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user_partial(user_id: int, user_data: UserUpdate, response: Response):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Obtener usuario existente
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El usuario con ID {user_id} no existe."
        )

    # Filtrar solo los campos enviados para la actualización parcial
    update_data = user_data.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se enviaron campos para actualizar."
        )

    # Actualizar campos específicos
    updated_user = user_service.update_user(user_id, {**user, **update_data})
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, response: Response):
    # Agregar cabeceras HTTP personalizadas
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"

    # Validar existencia y eliminar de la base de datos simulada
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El usuario con ID {user_id} no existe."
        )

    from app.data.users_db import users_db
    users_db.remove(user)
    
    # Retornar respuesta vacía (204 No Content)
    return None