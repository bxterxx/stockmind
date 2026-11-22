from Persistencia.Interfaces.UsuarioInterface import UsuarioInterface
from database import obtener_conexion


class UsuarioRepository(UsuarioInterface):
    def crear_usuario(self, id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Usuarios (id_usuario, nombre_completo, username, password, rol) VALUES (%s, %s, %s, %s, %s)",
                    (id_usuario, nombre_completo, username, password, rol)
                )
                conn.commit()
                return True

    def iniciar_sesion(self, username: str, password: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_usuario, nombre_completo, username, rol FROM Usuarios WHERE username = %s AND password = %s",
                    (username, password)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id": usuario[0], "nombre_completo": usuario[1], "username": usuario[2], "rol": usuario[3]}
                return None

    def actualizar_usuario(self, id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                if password:
                    cursor.execute(
                        "UPDATE Usuarios SET nombre_completo=%s, username=%s, password=%s, rol=%s WHERE id_usuario=%s",
                        (nombre_completo, username, password, rol, id_usuario)
                    )
                else:
                    cursor.execute(
                        "UPDATE Usuarios SET nombre_completo=%s, username=%s, rol=%s WHERE id_usuario=%s",
                        (nombre_completo, username, rol, id_usuario)
                    )
                conn.commit()
                return cursor.rowcount > 0

    def ver_perfil(self, id_usuario: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_usuario, nombre_completo, username, rol FROM Usuarios WHERE id_usuario = %s",
                    (id_usuario,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id": usuario[0], "nombre_completo": usuario[1], "username": usuario[2], "rol": usuario[3]}
                return None
            
    def eliminar_usuario(self, id_usuario: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Usuarios WHERE id_usuario = %s",
                    (id_usuario,)
                )
                conn.commit()
                return cursor.rowcount > 0
            
    def listar_usuarios(self):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_usuario, nombre_completo, username, rol FROM Usuarios",
                )
                usuarios = cursor.fetchall()
                return [{"id": row[0], "nombre_completo": row[1], "username": row[2], "rol": row[3]} for row in usuarios]