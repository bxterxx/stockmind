from sqlalchemy.orm import Session
from Entity.movimiento import MovimientoInventario
from Entity.producto import Producto
from fastapi import HTTPException
from datetime import datetime

def registrar_movimiento(db: Session, mov_data):
    # Validar existencia del producto
    producto = db.query(Producto).filter(Producto.id == mov_data.producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado para el movimiento")

    # Lógica de Stock Dinámica
    tipo_mov = mov_data.tipo.upper()
    if tipo_mov == "ENTRADA":
        producto.stock += mov_data.cantidad
    elif tipo_mov == "SALIDA":
        if producto.stock < mov_data.cantidad:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente. Disponible: {producto.stock}")
        producto.stock -= mov_data.cantidad
    else:
        raise HTTPException(status_code=400, detail="Tipo de movimiento inválido (Use ENTRADA o SALIDA)")

    # 3. Crear el registro histórico
    nuevo_mov = MovimientoInventario(
        producto_id=mov_data.producto_id,
        tipo=tipo_mov,
        cantidad=mov_data.cantidad,
        comentario=mov_data.comentario or f"Registro automático - {datetime.now().strftime('%Y-%m-%d')}"
    )
    
    db.add(nuevo_mov)
    db.commit()
    db.refresh(nuevo_mov)
    return nuevo_mov

def obtener_historial_producto(db: Session, producto_id: int):
    # Retorna movimientos ordenados por el más reciente
    return db.query(MovimientoInventario).filter(
        MovimientoInventario.producto_id == producto_id
    ).order_by(MovimientoInventario.fecha.desc()).all()