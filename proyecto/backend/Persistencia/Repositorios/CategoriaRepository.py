from database import obtener_conexion


class CategoriaRepository:
    
    def obtener_categorias(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre FROM Categorias")
                categorias = cursor.fetchall()
                return [{"id": row[0], "nombre": row[1]} for row in categorias]
            
    def obtener_categoria_por_id(self, categoria_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre FROM Categorias WHERE id = %s", (categoria_id,))
                categoria = cursor.fetchone()
                if categoria:
                    return {"id": categoria[0], "nombre": categoria[1]}
                return None

    def crear_categoria(self, categoria_id: int, nombre: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Categorias (id, nombre) VALUES (%s, %s)",
                    (categoria_id, nombre)
                )
                conn.commit()
                return {"message": f"Categoría {nombre} creada correctamente"}
        
    def eliminar_categoria(self, categoria_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Categorias WHERE id = %s",
                    (categoria_id,)
                )
                conn.commit()
                return {"message": f"Categoría {categoria_id} eliminada correctamente"}
        