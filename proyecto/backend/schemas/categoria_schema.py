from pydantic import BaseModel
from typing import Optional

class CategoriaCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    
    #Lo que devuelve
class CategoriaOut(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None

    class Config:
        from_attributes = True