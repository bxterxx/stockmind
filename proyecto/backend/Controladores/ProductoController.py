from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from proyecto.backend.Entidades import Productos

# Importas tus propios módulos
from database import obtener_conexion
from proyecto.backend.Esquemas.ProductoSchema import ProductoCreate, ProductoOut
from proyecto.backend.Servicios.ProductoService import ProductoService

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

#  OBTENER TODOS LOS PRODUCTOS
@router.get("/", response_model=List[ProductoOut])

def obtener_todos_productos(limit: int = 10):
    return ProductoService.Obtener_productos(limit)

# OBTENER UN PRODUCTO POR SU ID
@router.get("/{id}", response_model=ProductoOut)

def obtener_producto_por_el_id(id: int):
    producto = ProductoService.Obtener_productos_por_id(id)
    if not producto:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return producto

#  CREAR UN PRODUCTO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductoOut)

def crear_producto_nuevo(id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str, categoria_id: int):
    return ProductoService.Crear_producto(id, nombre, precio_venta, stock_actual, stock_minimo, descripcion, categoria_id)

# ELIMINAR UN PRODUCTO
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def eliminar_producto_por_id(id: int):
    success = ProductoService.Eliminar_producto (id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no encontrado")
    return None