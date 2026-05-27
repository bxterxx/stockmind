from fastapi import APIRouter, Body, HTTPException, status
from typing import List

from Servicios.CategoriaService import CategoriaService
from Esquemas.CategoriaSchema import CategoriaOut, CategoriaSchema 

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)
categoria_service = CategoriaService()

# obtener todas las categorías
@router.get("/", response_model=List[CategoriaOut])
def obtener_todas_categorias():
    return categoria_service.Obtener_categorias()

# obtener una categoría por ID
@router.get("/{id}", response_model=CategoriaOut)
def obtener_categoria_por_id(id: int):
    categoria = categoria_service.Obtener_categoria_por_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# crear una nueva categoría
@router.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)

def crear_categoria(categoria: CategoriaSchema = Body(...)):
    return categoria_service.Crear_categoria(categoria.id, categoria.nombre)

# eliminar una categoría
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(id: int):
    success = categoria_service.Eliminar_categoria(id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: Categoría no encontrada")
    return None