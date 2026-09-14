from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.dependencies.database_dependency import get_db
from app.services import user_service
from app.schemas.user_schema import (
    userCreate,
    userUpdate,
    userPatch,
    userResponse
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/",
    response_model=List[userResponse]
)
def obtener_usuarios(
    db: Session = Depends(get_db),
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: str = "asc"
):
    return user_service.obtener_usuarios(
        db=db,
        role=role,
        is_active=is_active,
        name=name,
        email=email,
        sort_by=sort_by,
        order=order
    )


@router.get(
    "/{user_id}",
    response_model=userResponse
)
def obtener_usuario(
    user_id: int,
    db: Session = Depends(get_db)
):
    usuario = user_service.obtener_usuario(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return usuario


@router.post("/",
             response_model=userResponse,
             status_code=status.HTTP_201_CREATED)
def crear_usuario(
    usuario_data: userCreate,
    db: Session = Depends(get_db)
):
    try:
        return user_service.crear_usuario(db, usuario_data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo electrónico ya está registrado"
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear el usuario"
        )


@router.put(
    "/{user_id}",
    response_model=userResponse
)
def actualizar_usuario(
    user_id: int,
    usuario_data: userUpdate,
    db: Session = Depends(get_db)
):
    usuario = user_service.obtener_usuario(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    try:
        return user_service.actualizar_usuario(db, user_id, usuario_data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo electrónico ya pertenece a otro usuario"
        )


@router.patch(
    "/{user_id}",
    response_model=userResponse
)
def actualizar_usuario_parcial(
    user_id: int,
    usuario_data: userPatch,
    db: Session = Depends(get_db)
):
    usuario = user_service.obtener_usuario(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    try:
        return user_service.actualizar_usuario_parcial(db, user_id, usuario_data)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo electrónico ya pertenece a otro usuario"
        )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_usuario(
    user_id: int,
    db: Session = Depends(get_db)
):
    usuario = user_service.eliminar_usuario(db, user_id)

    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

    return None