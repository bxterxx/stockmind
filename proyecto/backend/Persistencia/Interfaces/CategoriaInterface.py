from abc import abstractmethod

class CategoriaInterface:
    
    @abstractmethod
    def crear_categoria(self, categoria_id: int, nombre: str): pass
    
    @abstractmethod
    def eliminar_categoria(self, categoria_id: int): pass