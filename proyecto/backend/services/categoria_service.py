from sqlalchemy.orm import Session
from Entity.categoria import Categoria
from Entity.producto import Producto
from fastapi import HTTPException

def crear_categoria(db: Session, cat_data):
    nombre_norm = cat_data.nombre.strip().capitalize() # Normalizar el nombre (quitar espacios y capitalizar)
    existe = db.query(Categoria).filter(Categoria.nombre == nombre_norm).first()
    if existe:
        raise HTTPException(status_code=400, detail="Ya existe una categoría con ese nombre")

    nueva_cat = Categoria(nombre=nombre_norm, descripcion=cat_data.descripcion)
    db.add(nueva_cat)
    db.commit()
    db.refresh(nueva_cat)
    return nueva_cat

def eliminar_categoria(db: Session, cat_id: int):
    cat = db.query(Categoria).filter(Categoria.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    
    tiene_productos = db.query(Producto).filter(Producto.categoria_id == cat_id).first() # No borrar si tiene productos asociados
    if tiene_productos:
        raise HTTPException(status_code=400, detail="No se puede eliminar: existen productos vinculados a esta categoría")
    
    db.delete(cat)
    db.commit()
    return {"status": "success", "message": "Categoría eliminada"}