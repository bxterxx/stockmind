from proyecto.backend.Persistencia.Repositorios import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repositorio = UsuarioRepository()
        
    def crear_usuario(self, nombre: str, email: str, contraseña: str):
        if not nombre or not email or not contraseña:
            return {"message": "El nombre, email y contraseña son obligatorios"}
        
        usuario_existente = self.repositorio.obtener_usuario_por_email(email)
        if usuario_existente:
            return {"message": "Ya existe un usuario con este email"}
        
        nuevo_usuario = self.repositorio.crear_usuario(nombre, email, contraseña)
        return {"message": f"Usuario {nombre} creado correctamente", "usuario": nuevo_usuario}
    
    def obtener_usuario_por_email(self, email: str):
        if not email:
            return {"message": "El email es obligatorio"}
        
        usuario = self.repositorio.obtener_usuario_por_email(email)
        if not usuario:
            return {"message": f"Usuario con email {email} no encontrado"}
        return usuario