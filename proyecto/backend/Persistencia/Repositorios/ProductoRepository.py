from proyecto.backend.Entidades import Productos
from proyecto.backend.database import obtener_conexion


class ProductoRepository:
    def obtener_productos(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio_venta, stock_actual, stock_minimo, descripcion FROM Productos")
            return cursor.fetchall()
    
    def obtener_producto_por_id(self, producto_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio_venta, stock_actual, stock_minimo, descripcion FROM Productos WHERE id = %s", (producto_id,))
                return cursor.fetchone()
    
    def crear_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Productos (id, nombre, precio_venta, stock_actual, stock_minimo, descripcion) VALUES (%s, %s, %s, %s, %s, %s)",
                    (producto_id, nombre, precio_venta, stock_actual, stock_minimo, descripcion)
                )
                conn.commit()
                return self.obtener_producto_por_id(producto_id)
            
    def actualizar_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE Productos SET nombre = %s, precio_venta = %s, stock_actual = %s, stock_minimo = %s, descripcion = %s WHERE id = %s",
                    (nombre, precio_venta, stock_actual, stock_minimo, descripcion, producto_id)
                )
                conn.commit()
                return self.obtener_producto_por_id(producto_id)     
                   
    def eliminar_producto(self, producto_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Productos WHERE id = %s", (producto_id,))
                conn.commit()
                return {"message": f"Producto {producto_id} eliminado correctamente"}
            
    def buscar_productos_por_nombre(self, termino: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio_venta, stock_actual, stock_minimo, descripcion FROM Productos WHERE nombre ILIKE %s", ( "%" + termino + "%" ,))
                return cursor.fetchall()               
            
    def productos_bajo_stock(self, limite: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, precio_venta, stock_actual, stock_minimo, descripcion FROM Productos WHERE stock_actual <= %s", (limite,))
                return cursor.fetchall()
            
    def calcular_valor_total_stock(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT SUM(precio_venta * stock_actual) FROM Productos")
                return cursor.fetchone()[0]                