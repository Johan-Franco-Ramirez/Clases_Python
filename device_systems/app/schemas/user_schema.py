from pydantic import BaseModel, EmailStr, Field
from typing import Literal

# Modelo para validar los datos que llegan al crear un usuario (Fase 2)
class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, description="Nombre obligatorio, mínimo 3 caracteres")
    email: EmailStr = Field(..., description="Correo electrónico válido")
    role: Literal["admin", "support", "user"] = Field(..., description="Roles permitidos")
    is_active: bool = Field(default=True, description="Estado activo del usuario")

# Modelo de respuesta para la API (Fase 5)
class UserResponse(UserCreate):
    id: int = Field(..., description="ID único del usuario")

    class Config:
        from_attributes = True