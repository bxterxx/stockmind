from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship

class categoria:
    __tablename__ = "Categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    

    productos = relationship("Producto", back_populates="categoria")