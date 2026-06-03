from fastapi import APIRouter, status
from typing import List
from Servicios.MovimientoService import MovimientoService
from Esquemas.MovimientoSchema import MovimientoOut

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])
movimiento_service = MovimientoService()

# Registrar un movimiento (Entrada o Salida)
@router.post("/", response_model=MovimientoOut, status_code=status.HTTP_201_CREATED)

def crear_movimiento(id: int, Producto: int, Usuario: int, tipo: str, cantidad: int, fecha: str):
    return movimiento_service.Crear_movimiento(id=id, producto_id=Producto, id_usuario=Usuario, tipo=tipo, cantidad=cantidad, fecha=fecha)

# Listar historial de movimientos
@router.get("/", response_model=List[MovimientoOut])

def listar_movimientos():
    return movimiento_service.Listar_movimientos()

# Obtener movimientos de un producto específico
@router.get("/producto/{producto_id}", response_model=List[MovimientoOut])

def obtener_por_producto(producto_id: int):
    return movimiento_service.Obtener_por_producto(producto_id)

# Obtener un movimiento por su ID único
@router.get("/{id}", response_model=MovimientoOut)

def obtener_movimiento_por_id(id: int):
    return movimiento_service.Obtener_movimiento(id)