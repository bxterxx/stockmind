from Entidades.Proovedor import Proveedor
from database import obtener_conexion


class ProovedorRepository: 
    def listar_prooveedores(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_proveedor, nombre_empresa, telefono FROM Proveedores")
                proveedores = cursor.fetchall()
                return [{"id": row[0], "nombre_empresa": row[1], "telefono": row[2]} for row in proveedores]
        
    def crear_proveedor(self, id: int, nombre: str, contacto: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Proveedores (id_proveedor, nombre_empresa, telefono) VALUES (%s, %s, %s)",
                    (id, nombre, contacto)
                )
                conn.commit()
                return {"id": id, "nombre_empresa": nombre, "telefono": contacto}
    
    def eliminar_proveedor(self, id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Proveedores WHERE id_proveedor = %s", (id,))
                affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0