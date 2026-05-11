
from typing import Optional
from pydantic import BaseModel

class ProveedorBase(BaseModel):
    nombre: str
    contacto: Optional[str] = None
    email: str
    telefono: Optional[str] = None

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorOut(ProveedorBase):
    id: int
    class Config:
        from_attributes = True