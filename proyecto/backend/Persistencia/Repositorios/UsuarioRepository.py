from Entidades.Usuario import Usuario
from database import obtener_conexion


class UsuarioRepository:
    def crear_usuario(self, nombre: str, email: str, contraseña: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Usuarios (nombre, email, contraseña) VALUES (%s, %s, %s)",
                    (nombre, email, contraseña)
                )
                conn.commit()
                return {"nombre": nombre, "email": email, "contraseña": contraseña}

    def login(self, email: str, contraseña: str):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, email FROM Usuarios WHERE email = %s AND contraseña = %s",
                    (email, contraseña)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id": usuario[0], "nombre": usuario[1], "email": usuario[2]}
                return None

    def ver_perfil(self, usuario_id: int):
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, email FROM Usuarios WHERE id = %s",
                    (usuario_id,)
                )
                usuario = cursor.fetchone()
                if usuario:
                    return {"id": usuario[0], "nombre": usuario[1], "email": usuario[2]}
                return None