from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.utils.limiter import limiter

from app.schemas.auth_schema import UserRegister, UserResponse, Token

from app.auth.auth_service import register_user, authenticate_user
from app.auth.security import create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
@limiter.limit("3/minute")
def register(
    request: Request,
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db, user_data)


@router.post("/login", response_model=Token)
@limiter.limit("5/minute")
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }