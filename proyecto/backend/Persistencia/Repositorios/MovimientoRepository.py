from datetime import datetime

from proyecto.backend.Entidades.Movimiento import Movimiento


class MovimientoRepository:
    def __init__(self, db):
        self.db = db

    def registrar_movimiento(self, id: int, producto_id: int, tipo: str, cantidad: int, fecha):
        nuevo_movimiento = Movimiento(id=id, producto_id=producto_id, tipo=tipo, cantidad=cantidad, fecha=fecha)
        self.db.add(nuevo_movimiento)
        self.db.commit()
        return nuevo_movimiento
    
    def obtener_historial_producto(self, id: int, producto_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        movimientos = self.db.query(Movimiento).filter(
            Movimiento.producto_id == producto_id,
            Movimiento.fecha >= fecha_inicio,
            Movimiento.fecha <= fecha_fin
        ).all()
        return movimientos