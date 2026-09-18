from typing import Optional
from sqlalchemy.orm import Session
from app.models.user_model import user
from app.schemas.user_schema import userCreate, userUpdate, userPatch


def obtener_usuarios(
    db: Session,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    hashed_password: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: str = "asc"
):
    query = db.query(user)

    if role is not None:
        query = query.filter(user.role == role)

    if is_active is not None:
        query = query.filter(user.is_active == is_active)

    if name is not None:
        query = query.filter(user.name.ilike(f"%{name}%"))

    if email is not None:
        query = query.filter(user.email.ilike(f"%{email}%"))

    if hashed_password is not None:
        query = query.filter(user.hashed_password == hashed_password)

    if sort_by in ["name", "created_at"]:
        column = getattr(user, sort_by)
        if order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    return query.all()


def obtener_usuario(db: Session, usuario_id: int):
    return db.query(user).filter(user.id == usuario_id).first()


def crear_usuario(db: Session, usuario_data: userCreate):
    db_usuario = user(
        name=usuario_data.name,
        email=usuario_data.email,
        role=usuario_data.role,
        is_active=usuario_data.is_active
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


def actualizar_usuario(
    db: Session,
    usuario_id: int,
    usuario_data: userUpdate
):
    db_usuario = db.query(user).filter(user.id == usuario_id).first()

    if db_usuario:
        db_usuario.name = usuario_data.name  # type: ignore
        db_usuario.email = usuario_data.email  # type: ignore
        db_usuario.role = usuario_data.role  # type: ignore
        db_usuario.is_active = usuario_data.is_active  # type: ignore

        db.commit()
        db.refresh(db_usuario)

    return db_usuario


def actualizar_usuario_parcial(
    db: Session,
    usuario_id: int,
    usuario_data: userPatch
):
    db_usuario = db.query(user).filter(user.id == usuario_id).first()

    if db_usuario:
        if usuario_data.name is not None:
            db_usuario.name = usuario_data.name  # type: ignore

        if usuario_data.email is not None:
            db_usuario.email = usuario_data.email  # type: ignore

        if usuario_data.role is not None:
            db_usuario.role = usuario_data.role  # type: ignore

        if usuario_data.is_active is not None:
            db_usuario.is_active = usuario_data.is_active  # type: ignore

        db.commit()
        db.refresh(db_usuario)

    return db_usuario


def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(user).filter(user.id == usuario_id).first()

    if db_usuario:
        db.delete(db_usuario)
        db.commit()

    return db_usuario