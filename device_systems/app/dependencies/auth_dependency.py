from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.auth.security import decode_access_token
from app.models.user_model import user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> user:
    """Valida el token JWT y extrae el usuario actual de la base de datos."""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    email_val = payload.get("sub")

    if not isinstance(email_val, str) or not email_val:
        raise credentials_exception

    db_user = db.query(user).filter(user.email == email_val).first()

    if db_user is None:
        raise credentials_exception

    return db_user


def get_current_active_user(
    current_user: user = Depends(get_current_user)
) -> user:
    """Verifica que el usuario autenticado se encuentre activo."""

    # Forzamos la evaluación booleana por si el linter interpreta is_active como Column[bool]
    if not bool(current_user.is_active):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    return current_user


def require_admin_or_support(
    current_user: user = Depends(get_current_active_user)
) -> user:
    """Restringe el acceso a usuarios con rol 'admin' o 'support'."""

    # Forzamos la conversión a str para evitar conflictos de tipos con Column[str]
    user_role = str(current_user.role)

    if user_role not in ["admin", "support"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de administrador o soporte para esta acción."
        )

    return current_user