from fastapi import APIRouter, Body, HTTPException
from Servicios.CategoriaService import CategoriaService

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)
categoria_service = CategoriaService()

# obtener todas las categorías
@router.get("/")
def obtener_todas_categorias():
    return categoria_service.Obtener_categorias()

# obtener una categoría por ID
@router.get("/{id}")
def obtener_categoria_por_id(id: int):
    categoria = categoria_service.Obtener_categoria_por_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

# crear una nueva categoría
@router.post("/")

def crear_categoria(id: int, nombre: str):
    return categoria_service.Crear_categoria(id, nombre)

# eliminar una categoría
@router.delete("/{id}")
def eliminar_categoria(id: int):
    success = categoria_service.Eliminar_categoria(id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: Categoría no encontrada")
    return "Categoría eliminada exitosamente"