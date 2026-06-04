from Entidades import Productos
from database import obtener_conexion


class ProductoRepository:
    def obtener_productos(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Productos")
                productos = cursor.fetchall()
                return [{"id": row[0], "nombre": row[1], "precio_venta": row[2], "stock_actual": row[3], "stock_minimo": row[4], "categoria_id": row[5], "proveedor_id": row[6], "descripcion": row[7]} for row in productos]
            
    def obtener_producto_por_id(self, producto_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Productos WHERE id_producto = %s", (producto_id,))
                fila = cursor.fetchone()
                return {"id": fila[0], "nombre": fila[1], "precio_venta": fila[2], "stock_actual": fila[3], "stock_minimo": fila[4], "categoria_id": fila[5], "proveedor_id": fila[6], "descripcion": fila[7]} if fila else None

    def crear_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str, categoria_id: int, proveedor_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Productos (id_producto, nombre, precio_venta, stock_actual, stock_minimo, descripcion, id_categoria, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (producto_id, nombre, precio_venta, stock_actual, stock_minimo, descripcion, categoria_id, proveedor_id)
                )
            conn.commit()
            return {"message": f"Producto {nombre} creado correctamente con ID {producto_id}"}
            
    def eliminar_producto(self, producto_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Productos WHERE id_producto = %s", (producto_id,))
                affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0         
                      