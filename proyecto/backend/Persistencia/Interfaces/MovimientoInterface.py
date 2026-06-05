from abc import ABC, abstractmethod
from datetime import datetime


class MovimientoInterface(ABC):

    @abstractmethod
    def crear_movimiento(self, id: int, producto_id: int, id_usuario: int, tipo: str, cantidad: int, fecha: datetime):
        pass

    @abstractmethod
    def listar_movimientos(self):
        pass

    @abstractmethod
    def obtener_por_producto(self, producto_id: int):
        pass

    @abstractmethod
    def obtener_movimiento(self, id: int):
        pass