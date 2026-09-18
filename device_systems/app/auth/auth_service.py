from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user_model import user
from app.schemas.auth_schema import UserRegister
from app.auth.security import get_password_hash, verify_password


def register_user(db: Session, user_data: UserRegister) -> user:
    """Registra un nuevo usuario aplicando validación de email único y hash de contraseña."""
    existing_user = db.query(user).filter(user.email == user_data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya se encuentra registrado."
        )

    hashed_pwd = get_password_hash(user_data.password)

    new_user = user(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_pwd,
        role=user_data.role,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, email: str, password: str) -> user | None:
    """Verifica las credenciales del usuario (email y contraseña). Retorna el usuario o None."""
    db_user = db.query(user).filter(user.email == email).first()

    if not db_user:
        return None

    # Usamos str() para asegurar al linter que db_user.hashed_password se evalúa como texto plano
    if not verify_password(password, str(db_user.hashed_password)):
        return None

    return db_user