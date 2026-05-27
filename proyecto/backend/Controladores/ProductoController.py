from fastapi import APIRouter, Body, HTTPException, status
from typing import List

from Esquemas.ProductoSchema import ProductoOut, ProductoSchema
from Servicios.ProductoService import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)
producto_service = ProductoService()

#  OBTENER TODOS LOS PRODUCTOS
@router.get("/", response_model=List[ProductoOut])

def obtener_todos_productos():
    return producto_service.Obtener_productos()

# OBTENER UN PRODUCTO POR SU ID
@router.get("/{id}", response_model=ProductoOut)

def obtener_producto_por_el_id(id: int):
    producto = producto_service.Obtener_productos_por_id(id)
    if not producto:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return producto

#  CREAR UN PRODUCTO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductoOut)

def crear_producto_nuevo(producto: ProductoSchema = Body(...)):
    return producto_service.Crear_producto(
        producto.id,
        producto.nombre,
        producto.precio_venta,
        producto.stock_actual,
        producto.stock_minimo,
        producto.descripcion,
        producto.categoria_id,
        producto.proveedor_id
    )

# ELIMINAR UN PRODUCTO
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def eliminar_producto_por_id(id: int):
    success = producto_service.Eliminar_producto (id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return None