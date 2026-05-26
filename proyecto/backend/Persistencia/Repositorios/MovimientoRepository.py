from datetime import datetime

from proyecto.backend.Entidades.Movimiento import Movimiento
from proyecto.backend.database import obtener_conexion


class MovimientoRepository:

    def crear_movimiento(self, id: int, producto_id: int, tipo: str, cantidad: int, fecha: datetime):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Movimientos (id, producto_id, tipo, cantidad, fecha) VALUES (%s, %s, %s, %s, %s)",
                    (id, producto_id, tipo, cantidad, fecha)
                )
    
    def listar_movimientos(self, id: int, producto_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, producto_id, tipo, cantidad, fecha FROM Movimientos WHERE producto_id = %s AND fecha BETWEEN %s AND %s",
                    (producto_id, fecha_inicio, fecha_fin)
                )
                movimientos = cursor.fetchall()
                return [{"id": row[0], "producto_id": row[1], "tipo": row[2], "cantidad": row[3], "fecha": row[4]} for row in movimientos]
    
    def obtener_por_producto(self, producto_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, producto_id, tipo, cantidad, fecha FROM Movimientos WHERE producto_id = %s",
                    (producto_id,)
                )
                movimientos = cursor.fetchall()
                return [{"id": row[0], "producto_id": row[1], "tipo": row[2], "cantidad": row[3], "fecha": row[4]} for row in movimientos]
    
    def obtener_movimiento(self, id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, producto_id, tipo, cantidad, fecha FROM Movimientos WHERE id = %s",
                    (id,)
                )
                row = cursor.fetchone()
                if row:
                    return {"id": row[0], "producto_id": row[1], "tipo": row[2], "cantidad": row[3], "fecha": row[4]}
                return None