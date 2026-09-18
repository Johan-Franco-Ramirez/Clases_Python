import re

from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict

class UserRegister(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
    role: str = Field(default="user")

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        """Valida que la contraseña cumpla con los requisitos de seguridad."""
        if " " in v:
            raise ValueError("La contraseña no puede contener espacios en blanco.")
        if not re.search(r"[A-Z]", v):
            raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", v):
            raise ValueError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r"\d", v):
            raise ValueError("La contraseña debe contener al menos un número.")
        return v

    @field_validator("role")
    @classmethod
    def validate_role(cls, v: str) -> str:
        """Valida que el rol asignado sea uno de los permitidos."""
        allowed_roles = ["admin", "support", "user"]
        if v not in allowed_roles:
            raise ValueError(f"El rol debe ser uno de los siguientes: {allowed_roles}")
        return v


class UserLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    role: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    
    # Configuración de Pydantic v2 para permitir la lectura desde modelos ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)