from pydantic import BaseModel
from datetime import datetime
from typing import Union

class MovimientoBase(BaseModel):
    producto_id: int
    cantidad: int
    tipo: str  # "ENTRADA" o "SALIDA"

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoOut(MovimientoBase):
    id: int
    producto_id: int
    tipo: str
    cantidad: int
    fecha: Union[datetime, str]

    class Config:
        from_attributes = True