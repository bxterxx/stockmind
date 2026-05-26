from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from proyecto.backend.Servicios import MovimientoService
from proyecto.backend.Esquemas.MovimientoSchema import MovimientoCreate, MovimientoOut

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])

# Registrar un movimiento (Entrada o Salida)
@router.post("/", response_model=MovimientoOut, status_code=status.HTTP_201_CREATED)
def crear_movimiento(data: MovimientoCreate, db: Session = Depends(get_db)):
    return MovimientoService.create(db, data)

# Listar historial de movimientos
@router.get("/", response_model=List[MovimientoOut])
def listar_movimientos(db: Session = Depends(get_db)):
    return MovimientoService.get_all(db)

# Obtener movimientos de un producto específico
@router.get("/producto/{producto_id}", response_model=List[MovimientoOut])
def obtener_por_producto(producto_id: int, db: Session = Depends(get_db)):
    return MovimientoService.get_by_product(db, producto_id)

# Obtener un movimiento por su ID único
@router.get("/{id}", response_model=MovimientoOut)
def obtener_movimiento(id: int, db: Session = Depends(get_db)):
    db_mov = MovimientoService.get_by_id(db, id)
    if not db_mov:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return db_mov