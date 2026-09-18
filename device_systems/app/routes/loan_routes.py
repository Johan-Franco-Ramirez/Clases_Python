from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies.database_dependency import get_db
from app.dependencies.auth_dependency import (
    get_current_active_user, 
    require_admin_or_support
)

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/", summary="Crear un nuevo préstamo")
def create_loan(
    loan_data: dict, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_active_user)
):
    """
    Registrar un nuevo préstamo de dispositivo. 
    Requiere autenticación (cualquier usuario activo).
    """
    # Lógica base del endpoint de préstamos
    return {
        "message": "Préstamo registrado exitosamente",
        "user_email": current_user.email,
        "data": loan_data
    }

@router.patch("/{loan_id}/return", summary="Registrar devolución de un préstamo")
def return_loan(
    loan_id: int, 
    db: Session = Depends(get_db), 
    current_user = Depends(require_admin_or_support)
):
    """
    Marcar un préstamo como devuelto.
    Requiere rol de Administrador o Soporte.
    """
    return {
        "message": f"Préstamo con ID {loan_id} marcado como devuelto",
        "updated_by": current_user.email
    }

@router.get("/details", summary="Obtener detalles avanzados de préstamos")
def get_loan_details(
    db: Session = Depends(get_db), 
    current_user = Depends(require_admin_or_support)
):
    """
    Consultar detalles y reportes de préstamos.
    Requiere rol de Administrador o Soporte.
    """
    return {
        "message": "Lista detallada de préstamos",
        "loans": []
    }