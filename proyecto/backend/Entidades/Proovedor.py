from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Proveedor:
    __tablename__ = "Proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre_empresa = Column(String, unique=True, nullable=False)
    telefono = Column(String)

    productos = relationship("Producto", back_populates="proveedor")