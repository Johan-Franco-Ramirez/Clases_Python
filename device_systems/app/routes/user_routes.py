from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.database_dependency import get_db
from app.models.user_model import user
from app.dependencies.auth_dependency import get_current_active_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users(db: Session = Depends(get_db), current_user: user = Depends(get_current_active_user)):
    """Lista todos los usuarios (Requiere autenticación)."""
    # Tu lógica anterior de consulta de usuarios...
    pass

@router.get("/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db), current_user: user = Depends(get_current_active_user)):
    """Obtiene un usuario por ID (Requiere autenticación)."""
    # Tu lógica anterior...
    pass