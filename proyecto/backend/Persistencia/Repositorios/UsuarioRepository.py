from proyecto.backend.Entidades.Usuario import Usuario


class UsuarioRepository:
    def __init__(self, db):
        self.db = db

    def crear_usuario(self, nombre: str, email: str, contraseña: str):
        nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=contraseña)
        self.db.add(nuevo_usuario)
        self.db.commit()
        return nuevo_usuario

    def obtener_usuario_por_email(self, email: str):
        return self.db.query(Usuario).filter(Usuario.email == email).first()