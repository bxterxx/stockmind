from pydantic import BaseModel
from typing import Optional

class CategoriaSchema(BaseModel):
    id: int
    nombre: str
    
class CategoriaOut(BaseModel):
    id: int
    nombre: str

class Config:
    from_attributes = True