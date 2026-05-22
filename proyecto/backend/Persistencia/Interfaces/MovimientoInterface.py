from abc import abstractmethod
from datetime import datetime


class MovimientoInterface:
    
    @abstractmethod
    def registrar_movimiento(self, id: int, Producto_id: int, tipo: str, cantidad: int, fecha: datetime):
        pass

    @abstractmethod
    def obtener_historial_producto(self, id: int, Producto_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        pass