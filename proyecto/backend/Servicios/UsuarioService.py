from Persistencia.Repositorios.UsuarioRepository import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repositorio = UsuarioRepository()
        
    def Crear_usuario(self, id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
        if not nombre_completo or not password or not rol:
            return {"message": "El nombre completo, contraseña y rol son obligatorios"}

        nuevo_usuario = self.repositorio.crear_usuario(id_usuario=id_usuario, nombre_completo=nombre_completo, username=username, password=password, rol=rol)
        if nuevo_usuario:
            return {
                "id_usuario": id_usuario,
                "nombre_completo": nombre_completo,
                "username": username,
                "rol": rol
            }
    
    def Login(self, email: str, contraseña: str):
        if not email or not contraseña:
            return {"message": "El email y la contraseña son obligatorios"}
        
        usuario = self.repositorio.login(email, contraseña)
        if usuario:
            return {"message": f"Usuario {usuario} autenticado correctamente"}
        else:
            return {"message": "Credenciales inválidas"}
        
    def Ver_perfil(self, id_usuario: int):
        usuario = self.repositorio.ver_perfil(id_usuario)
        if usuario:
            return usuario
        else:
            return {"message": f"Usuario con ID {id_usuario} no encontrado"}