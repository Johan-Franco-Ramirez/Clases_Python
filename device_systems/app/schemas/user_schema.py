from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional

class UserCreate(BaseModel):
    # Validar datos de entrada para la creación
    name: str = Field(..., min_length=3, description="Nombre obligatorio, mínimo 3 caracteres")
    email: EmailStr = Field(..., description="Correo electrónico válido")
    role: Literal["admin", "support", "user"] = Field(..., description="Roles permitidos")
    is_active: bool = Field(default=True, description="Estado activo del usuario")

class UserUpdate(BaseModel):
    # Validar datos opcionales para la actualización parcial
    name: Optional[str] = Field(None, min_length=3, description="Nombre opcional")
    email: Optional[EmailStr] = Field(None, description="Correo electrónico opcional")
    role: Optional[Literal["admin", "support", "user"]] = Field(None, description="Rol opcional")
    is_active: Optional[bool] = Field(None, description="Estado opcional")

class UserResponse(UserCreate):
    # Esquema de respuesta con ID incluido
    id: int = Field(..., description="ID único del usuario")

    class Config:
        from_attributes = True