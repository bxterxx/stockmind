from abc import abstractmethod
from datetime import datetime


class MovimientoInterface:
    
    @abstractmethod
    def crear_movimiento(self, id: int, producto_id: int, tipo: str, cantidad: int, fecha: datetime):
        pass

    @abstractmethod
    def listar_movimientos(self, id: int, producto_id: int, fecha_inicio: datetime, fecha_fin: datetime):
        pass
    
    @abstractmethod
    def obtener_por_producto(self, producto_id: int):
        pass
    
    @abstractmethod
    def obtener_movimiento(self, id: int):
        pass