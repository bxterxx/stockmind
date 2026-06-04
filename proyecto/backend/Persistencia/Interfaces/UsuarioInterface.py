from abc import abstractmethod


class UsuarioInterface:
    
    @abstractmethod
    def crear_usuario(self, nombre: str, email: str, contraseña: str):
        pass

    @abstractmethod
    def ver_perfil(self, id_usuario: int):
        pass
    
