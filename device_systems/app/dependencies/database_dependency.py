from app.data.connection import SessionLocal

def get_db():
    """
    Dependencia de FastAPI: abre una sesión, se la entrega al endpoint,
    y la cierra automáticamente al terminar (incluso si hay un error).

    Se usa así en un endpoint:

        @app.get("/algo")
        def leer_algo(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()