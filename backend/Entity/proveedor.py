from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.Entity.producto import Base


class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre_empresa = Column(String, unique=True, nullable=False)
    contacto_nombre = Column(String)
    telefono = Column(String)
    email = Column(String)

    productos = relationship("Producto", back_populates="proveedor")