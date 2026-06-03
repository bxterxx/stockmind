from Entidades.Usuario import Usuario
from database import obtener_conexion


class UsuarioRepository:
    def crear_usuario(self, id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Usuarios (id_usuario, nombre_completo, username, password, rol) VALUES (%s, %s, %s, %s, %s)",
                    (id_usuario, nombre_completo, username, password, rol)
                )
                conn.commit()
                return True

    def login(self, username: str, password: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_usuario, nombre_completo, username FROM Usuarios WHERE username = %s AND password = %s",
                    (username, password)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id_usuario": usuario[0], "nombre_completo": usuario[1], "username": usuario[2]}
                return None

    def ver_perfil(self, id_usuario: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id_usuario, nombre_completo, username FROM Usuarios WHERE id_usuario = %s",
                    (id_usuario,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id_usuario": usuario[0], "nombre_completo": usuario[1], "username": usuario[2]}
                return None