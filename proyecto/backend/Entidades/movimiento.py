from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Movimiento:
    __tablename__ = "Movimientos"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("Productos.id_producto"))
    tipo = Column(String)  # "ENTRADA" o "SALIDA"
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    producto = relationship("Producto", back_populates="movimientos")