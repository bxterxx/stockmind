from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from proyecto.backend.Entity.producto import producto

# Importas tus propios módulos
from ..database import get_db
from ..schemas import ProductCreate, ProductOut

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

#  OBTENER TODOS LOS PRODUCTOS
@router.get("/", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db), limit: int = 10):
    products = db.query(producto).limit(limit).all()
    return products

#  CREAR UN PRODUCTO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    new_product = producto(**payload.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# ELIMINAR UN PRODUCTO
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    product_query = db.query(producto).filter(producto.id == id)
    
    if product_query.first() is None:
        raise HTTPException(status_code=404, detail=f"Producto con id {id} no existe")
    
    product_query.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Producto con id {id} eliminado exitosamente"}