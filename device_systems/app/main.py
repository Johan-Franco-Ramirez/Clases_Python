from fastapi import FastAPI
from app.data.connection import engine, Base
from app.routes.user_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de gestion usuarios device_systems"
)

app.include_router(router)