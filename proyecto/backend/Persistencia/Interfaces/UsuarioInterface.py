from abc import abstractmethod


class UsuarioInterface:
    
    @abstractmethod
    def registrar_usuario(self, nombre: str, email: str, contraseña: str):
        pass

    @abstractmethod
    def autenticar_usuario(self, email: str, contraseña: str):
        pass