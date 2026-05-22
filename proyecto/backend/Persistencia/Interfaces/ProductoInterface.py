from abc import abstractmethod

class ProductoInterface:
    
    @abstractmethod
    def obtener_productos(self): pass
    
    @abstractmethod
    def obtener_producto_por_id(self, producto_id: int): pass
    
    @abstractmethod
    def crear_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str): pass

    @abstractmethod
    def actualizar_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str): pass

    @abstractmethod
    def eliminar_producto(self, producto_id: int): pass
    
    @abstractmethod
    def buscar_productos_por_nombre(self, termino: str): pass
    
    @abstractmethod
    def productos_bajo_stock(self, limite: int): pass
    
    @abstractmethod
    def calcular_valor_total_stock(self): pass