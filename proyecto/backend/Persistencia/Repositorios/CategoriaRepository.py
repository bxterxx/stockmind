from Persistencia.Interfaces.CategoriaInterface import CategoriaInterface
from database import obtener_conexion


class CategoriaRepository(CategoriaInterface):
    
    def obtener_categorias(self, id: int = None, nombre: str = None):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_categoria, nombre FROM Categorias")
                categorias = cursor.fetchall()
                return [{"id": row[0], "nombre": row[1]} for row in categorias]
            
    def obtener_categoria_por_id(self, categoria_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_categoria, nombre FROM Categorias WHERE id_categoria = %s", (categoria_id,))
                categoria = cursor.fetchone()
                if categoria:
                    return {"id": categoria[0], "nombre": categoria[1]}
                return None

    def crear_categoria(self, categoria_id: int, nombre: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Categorias (id_categoria, nombre) VALUES (%s, %s)",
                    (categoria_id, nombre)
                )
                conn.commit()
            return True
        
    def eliminar_categoria(self, categoria_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Categorias WHERE id_categoria = %s",
                    (categoria_id,)
                )
                affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0
