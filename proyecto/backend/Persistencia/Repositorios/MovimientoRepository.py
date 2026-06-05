from Persistencia.Interfaces.MovimientoInterface import MovimientoInterface
from datetime import datetime

from Entidades.Movimiento import Movimiento
from database import obtener_conexion


class MovimientoRepository(MovimientoInterface):
    
    def crear_movimiento(self, id: int, producto_id: int, id_usuario: int, tipo: str, cantidad: int, fecha: datetime):
        with obtener_conexion() as conn:
             with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Movimientos (id_movimiento, id_producto, id_usuario, tipo, cantidad, fecha) VALUES (%s, %s, %s, %s, %s, %s)",
                    (id, producto_id, id_usuario, tipo, cantidad, fecha)
                )
                return True

    def listar_movimientos(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_movimiento, id_producto, id_usuario, tipo, cantidad, fecha FROM Movimientos",
                )
                movimientos = cursor.fetchall()
                return [
                {
                    "id": row[0],
                    "producto_id": row[1],
                    "id_usuario": row[2],
                    "tipo": row[3],
                    "cantidad": row[4],
                    "fecha": str(row[5])
                } 
               for row in movimientos
            ]

    def obtener_por_producto(self, producto_id: int):
        with obtener_conexion() as conn:
           with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_movimiento, id_producto, id_usuario, tipo, cantidad, fecha FROM Movimientos WHERE id_producto = %s",
                    (producto_id,)
                )
                movimientos = cursor.fetchall()
                return [{"id": row[0], "producto_id": row[1], "id_usuario": row[2], "tipo": row[3], "cantidad": row[4], "fecha": str(row[5])} for row in movimientos]

    def obtener_movimiento(self, id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_movimiento, id_producto, id_usuario, tipo, cantidad, fecha FROM Movimientos WHERE id_movimiento = %s",
                    (id,)
                )
                row = cursor.fetchone()
                if row:
                    return {"id": row[0], "producto_id": row[1], "id_usuario": row[2], "tipo": row[3], "cantidad": row[4], "fecha": str(row[5])}
                return None

    def eliminar_movimiento(self, id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Movimientos WHERE id_movimiento = %s", (id,))
                affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0