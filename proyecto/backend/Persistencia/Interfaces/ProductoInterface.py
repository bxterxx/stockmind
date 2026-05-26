from abc import abstractmethod

class ProductoInterface:
    
    @abstractmethod
    def obtener_productos(self): pass
    
    @abstractmethod
    def obtener_producto_por_id(self, producto_id: int): pass
    
    @abstractmethod
    def crear_producto(self, producto_id: int, nombre: str, categoria_id: int, precio: float, stock: int): pass
    
    @abstractmethod
    def eliminar_producto(self, producto_id: int): pass