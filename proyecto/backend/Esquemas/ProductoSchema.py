from pydantic import BaseModel
from typing import Optional

class ProductoSchema(BaseModel):
    id: int
    nombre: str
    precio_venta: float
    stock_actual: int
    stock_minimo: int
    descripcion: str
    categoria_id: int
    proveedor_id: int

class ProductoOut(BaseModel):
    id: int
    nombre: str
    precio_venta: float
    stock_actual: int
    stock_minimo: int
    descripcion: str
    categoria_id: int
    prooveedor_id: int

    class Config:
        from_attributes = True