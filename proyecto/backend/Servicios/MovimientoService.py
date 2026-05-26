from proyecto.backend.Persistencia.Repositorios.MovimientoRepository import MovimientoRepository


class MovimientoService:
    def __init__(self):
        self.repositorio = MovimientoRepository()

    def registrar_movimiento(self, id: int, producto_id: int, tipo: str, cantidad: int, fecha):
        nuevo_movimiento = self.repositorio.registrar_movimiento(id, producto_id, tipo, cantidad, fecha)
        return nuevo_movimiento
    
    def obtener_historial_producto(self, id: int, producto_id: int, fecha_inicio, fecha_fin):
        movimientos = self.repositorio.obtener_historial_producto(id, producto_id, fecha_inicio, fecha_fin)
        return movimientos
