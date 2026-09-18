from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.database_dependency import get_db
from app.models.user_model import user
from app.dependencies.auth_dependency import (
    get_current_active_user, 
    require_admin_or_support
)

router = APIRouter(prefix="/devices", tags=["Devices"])

@router.post("/")
def create_device(
    device_data: dict, 
    db: Session = Depends(get_db), 
    current_user: user = Depends(require_admin_or_support)
):
    """Crear dispositivo (Solo Admin o Support)."""
    pass

@router.put("/{device_id}")
def update_device(
    device_id: int, 
    device_data: dict, 
    db: Session = Depends(get_db), 
    current_user: user = Depends(require_admin_or_support)
):
    """Actualizar dispositivo (Solo Admin o Support)."""
    pass

@router.delete("/{device_id}")
def delete_device(
    device_id: int, 
    db: Session = Depends(get_db), 
    current_user: user = Depends(get_current_active_user)
):
    """Eliminar dispositivo (Exclusivo Admin)."""
    # Si requieres estrictamente que solo sea admin puro, asegúrate de tener la función require_admin en auth_dependency
    if str(current_user.role) != "admin":
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Se requiere rol de administrador exclusivo para eliminar dispositivos."
        )
    pass