from sqlalchemy.orm import Session
from backend.Entity.producto import Producto
from backend.Entity.categoria import Categoria
from backend.Entity.proveedor import Proveedor
from fastapi import HTTPException

def obtener_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail=f"Producto con ID {producto_id} no encontrado")
    return producto

def crear_producto(db: Session, producto_data):
    # Validar Categoría
    cat = db.query(Categoria).filter(Categoria.id == producto_data.categoria_id).first()
    if not cat:
        raise HTTPException(status_code=400, detail="La categoría especificada no existe")
    
    # Validar Proveedor
    prov = db.query(Proveedor).filter(Proveedor.id == producto_data.proveedor_id).first()
    if not prov:
        raise HTTPException(status_code=400, detail="El proveedor especificado no existe")

    # Crear instancia
    nuevo_producto = Producto(**producto_data.dict())
    
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def actualizar_producto(db: Session, producto_id: int, datos_nuevos):
    db_producto = obtener_producto_por_id(db, producto_id)
    
    update_data = datos_nuevos.dict(exclude_unset=True) 
    for key, value in update_data.items():
        setattr(db_producto, key, value)
    
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = obtener_producto_por_id(db, producto_id)
    db.delete(db_producto)
    db.commit()
    return {"message": f"Producto {producto_id} eliminado correctamente"}

def buscar_productos_por_nombre(db: Session, termino: str):
    return db.query(Producto).filter(Producto.nombre.contains(termino)).all()

def productos_bajo_stock(db: Session, limite: int = 5):

    return db.query(Producto).filter(Producto.stock <= limite).all()

def calcular_valor_total_stock(db: Session):
    productos = db.query(Producto).all()
    total = sum(p.precio * p.stock for p in productos)
    return {
        "cantidad_articulos": len(productos),
        "valor_total_inventario": round(total, 2)
    }