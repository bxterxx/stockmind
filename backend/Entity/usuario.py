from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hashed = Column(String, nullable=False) # Nunca guardar en texto plano
    rol = Column(String, default="empleado") # admin o empleado
    activo = Column(Boolean, default=True)