from operator import mod

from fastapi import APIRouter, Body, HTTPException, status
import Esquemas.ProductoSchema as esquemas_producto

from Esquemas.ProductoSchema import ProductoOut
from Servicios.ProductoService import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)
producto_service = ProductoService()

#  OBTENER TODOS LOS PRODUCTOS
@router.get("/")

def obtener_todos_productos():
    return producto_service.Obtener_productos()

# OBTENER UN PRODUCTO POR SU ID
@router.get("/{id}")

def obtener_producto_por_el_id(id: int):
    producto_por_id = producto_service.Obtener_productos_por_id(id)
    if not producto_por_id:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return producto_por_id

#  CREAR UN PRODUCTO
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto_nuevo(id_producto: int = Body(...), nombre: str = Body(...), precio_venta: float = Body(...), stock_actual: int = Body(...), stock_minimo: int = Body(...), descripcion: str = Body(...), categoria_id: int = Body(...), proveedor_id: int = Body(...)):
    return producto_service.Crear_producto(id_producto, nombre, precio_venta, stock_actual, stock_minimo, descripcion, categoria_id, proveedor_id)

# ELIMINAR UN PRODUCTO
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def eliminar_producto_por_id(id: int):
    success = producto_service.Eliminar_producto (id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return "Producto eliminado exitosamente"