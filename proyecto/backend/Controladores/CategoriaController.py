from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importaciones siguiendo tu estructura de carpetas
from database import get_db
from proyecto.backend.Servicios import CategoriaService
from proyecto.backend.Esquemas.CategoriaSchema import CategoriaCreate, CategoriaOut # Deberás crear este archivo

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

# obtener todas las categorías
@router.get("/", response_model=List[CategoriaOut])
def read_categorias(db: Session = Depends(get_db)):
    return CategoriaService.get_all(db)

# obtener una categoría por ID
@router.get("/{id}", response_model=CategoriaOut)
def read_categoria(id: int, db: Session = Depends(get_db)):
    db_categoria = CategoriaService.get_by_id(db, id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return db_categoria

# crear una nueva categoría
@router.post("/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED)
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return CategoriaService.create(db, categoria)

# eliminar una categoría
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categoria(id: int, db: Session = Depends(get_db)):
    success = CategoriaService.delete(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: Categoría no encontrada")
    return None