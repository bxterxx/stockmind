from abc import abstractmethod


class ProovedorInterface:
    
    @abstractmethod
    def listar_proveedores(self):
        pass
    
    @abstractmethod
    def crear_proveedor(self, id: int, nombre: str, contacto: str):
        pass