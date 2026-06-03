import datetime

from Persistencia.Repositorios.MovimientoRepository import MovimientoRepository


class MovimientoService:
    def __init__(self):
        self.repositorio = MovimientoRepository()

    def Crear_movimiento(self, id: int, producto_id: int, id_usuario: int, tipo: str, cantidad: int, fecha):
        
        tipo_movimiento = tipo.upper()
        if not id or not producto_id or not id_usuario or not tipo or cantidad is None or not fecha:
            return {"message": "Todos los campos son obligatorios"}
        
        if tipo_movimiento not in ["ENTRADA", "SALIDA"]:
            raise ValueError("El tipo de movimiento debe ser 'ENTRADA' o 'SALIDA'")
        
        movimiento_creado = self.repositorio.crear_movimiento(id, producto_id, id_usuario, tipo, cantidad, fecha)
        
        if movimiento_creado:
            return {"message": f"Movimiento creado correctamente con ID {id}"}
        else:
            return {"message": "Error al crear el movimiento"}
        
    def Listar_movimientos(self, id: int, producto_id: int, id_usuario: int, fecha_inicio: datetime, fecha_fin: datetime):
        movimientos = self.repositorio.listar_movimientos(id, producto_id, id_usuario, fecha_inicio, fecha_fin)
        return movimientos
    
    def Obtener_por_producto(self, producto_id: int):
        movimientos = self.repositorio.obtener_por_producto(producto_id)
        return movimientos
    
    def Obtener_movimiento(self, id: int):
        movimiento = self.repositorio.obtener_movimiento(id)
        if movimiento:
            return movimiento
        return {"message": f"Movimiento con ID {id} no encontrado"}
