from proyecto.backend.database import obtener_conexion


class CategoriaRepository:

    def Crear_categoria(self, categoria_id: int, nombre: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Categorias (id, nombre) VALUES (%s, %s)",
                    (categoria_id, nombre)
                )
                conn.commit()
                return {"message": f"Categoría {nombre} creada correctamente"}
        
    def Eliminar_categoria(self, categoria_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Categorias WHERE id = %s",
                    (categoria_id,)
                )
                conn.commit()
                return {"message": f"Categoría {categoria_id} eliminada correctamente"}    
            db.delete(categoria_a_eliminar)
            db.commit()
            return {"message": f"Categoría {categoria_id} eliminada correctamente"}    
        