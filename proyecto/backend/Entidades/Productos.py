from sqlalchemy import Column, Float, ForeignKey, Integer, String

from Entidades import Categoria

class producto:
    __tablename__ = "Productos"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio_venta = Column(Float)
    stock_actual = Column(Integer)
    stock_minimo = Column(Integer)
    descripcion = Column(String)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))