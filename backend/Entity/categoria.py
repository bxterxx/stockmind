from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    

    productos = relationship("Producto", back_populates="categoria")