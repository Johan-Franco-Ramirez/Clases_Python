from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.data.connection import Base

class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    
    # Agregamos server_default para que SQLite sepas qué ponerle a los registros antiguos
    hashed_password = Column(String, nullable=False, server_default="temp_hash_placeholder")
    role = Column(String, nullable=False, server_default="user")
    is_active = Column(Boolean, default=True, server_default="1", nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)