from abc import ABC, abstractmethod


class UsuarioInterface(ABC):

    @abstractmethod
    def crear_usuario(self, id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
        pass

    @abstractmethod
    def ver_perfil(self, id_usuario: int):
        pass
    
    @abstractmethod
    def eliminar_usuario(self, id_usuario: int):
        pass
    
    @abstractmethod
    def listar_usuarios(self):
        pass
