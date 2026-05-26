from abc import abstractmethod


class ProovedorInterface:
    
    @abstractmethod
    def crear_proveedor(self, id: int, nombre: str, contacto: str):
        pass
    
    @abstractmethod
    def obtener_catalogo_proveedor(self, id: int):
        pass