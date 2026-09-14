from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.data.connection import SessionLocal, Base

class user (Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
