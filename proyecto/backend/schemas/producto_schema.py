from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    categoria_id: int  

class ProductoCreate(ProductoBase):
    pass 

class ProductoOut(ProductoBase):
    id: int

    class Config:
        # Leer los datos del Entity
        from_attributes = True