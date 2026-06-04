from fastapi import APIRouter, HTTPException
from Servicios.MovimientoService import MovimientoService

router = APIRouter(prefix="/movimientos", tags=["Movimientos"])
movimiento_service = MovimientoService()

# Registrar un movimiento (Entrada o Salida)
@router.post("/")

def crear_movimiento(id: int, Producto: int, Usuario: int, tipo: str, cantidad: int, fecha: str):
    return movimiento_service.Crear_movimiento(id=id, producto_id=Producto, id_usuario=Usuario, tipo=tipo, cantidad=cantidad, fecha=fecha)

# Listar historial de movimientos
@router.get("/")

def listar_movimientos():
    return movimiento_service.Listar_movimientos()

# Obtener movimientos de un producto específico
@router.get("/producto/{producto_id}")

def obtener_por_producto(producto_id: int):
    return movimiento_service.Obtener_por_producto(producto_id)

# Obtener un movimiento por su ID único
@router.get("/{id}")

def obtener_movimiento_por_id(id: int):
    return movimiento_service.Obtener_movimiento(id)

# Eliminar un movimiento
@router.delete("/{id}")
def eliminar_movimiento(id: int):
    success = movimiento_service.Eliminar_movimiento(id)
    if not success:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    return {"message": "Movimiento eliminado exitosamente"}