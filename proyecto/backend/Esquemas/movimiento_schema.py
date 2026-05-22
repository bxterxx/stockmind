from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MovimientoBase(BaseModel):
    producto_id: int
    cantidad: int
    tipo: str  # "ENTRADA" o "SALIDA"
    motivo: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class MovimientoOut(MovimientoBase):
    id: int
    fecha: datetime # Se genera automáticamente en la DB

    class Config:
        from_attributes = True