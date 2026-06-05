from abc import ABC, abstractmethod


class ProductoInterface(ABC):

    @abstractmethod
    def obtener_productos(self):
        pass

    @abstractmethod
    def obtener_producto_por_id(self, producto_id: int):
        pass

    @abstractmethod
    def crear_producto(self, producto_id: int, nombre: str, precio_venta: float, stock_actual: int, stock_minimo: int, descripcion: str, categoria_id: int, proveedor_id: int):
        pass

    @abstractmethod
    def eliminar_producto(self, producto_id: int):
        pass