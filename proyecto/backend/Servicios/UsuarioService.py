from Persistencia.Repositorios.UsuarioRepository import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repositorio = UsuarioRepository()
        
    def Crear_usuario(self, id: int, nombre: str, email: str, contraseña: str):
        if not nombre or not email or not contraseña:
            return {"message": "El nombre, email y contraseña son obligatorios"}
    
        nuevo_usuario = self.repositorio.crear_usuario(id, nombre, email, contraseña) 
        return {"message": f"Usuario {nuevo_usuario} creado correctamente"}
    
    def Login(self, email: str, contraseña: str):
        if not email or not contraseña:
            return {"message": "El email y la contraseña son obligatorios"}
        
        usuario = self.repositorio.login(email, contraseña)
        if usuario:
            return {"message": f"Usuario {usuario} autenticado correctamente"}
        else:
            return {"message": "Credenciales inválidas"}
        
    def Ver_perfil(self, id: int):
        usuario = self.repositorio.ver_perfil(id)
        if usuario:
            return usuario
        else:
            return {"message": f"Usuario con ID {id} no encontrado"}