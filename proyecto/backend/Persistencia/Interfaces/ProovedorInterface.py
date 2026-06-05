from abc import ABC, abstractmethod


class ProovedorInterface(ABC):

    @abstractmethod
    def listar_prooveedores(self):
        pass

    @abstractmethod
    def crear_proveedor(self, id: int, nombre: str, contacto: str):
        pass