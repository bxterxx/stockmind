from pydantic import BaseModel

class ProductoSchema(BaseModel):
    id_producto: int
    nombre: str
    precio_venta: float
    stock_actual: int
    stock_minimo: int
    descripcion: str
    categoria_id: int
    prooveedor_id: int

class ProductoOut(BaseModel):
    id_producto: int
    nombre: str
    precio_venta: float
    stock_actual: int
    stock_minimo: int
    descripcion: str
    categoria_id: int
    prooveedor_id: int

class Config:
    from_attributes = True