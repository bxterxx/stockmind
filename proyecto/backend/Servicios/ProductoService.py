from Persistencia.Repositorios.ProductoRepository import ProductoRepository


class ProductoService:
    def __init__(self):
        self.repositorio = ProductoRepository()
        
    def Obtener_productos(self):
        return self.repositorio.obtener_productos()
    
    def Obtener_productos_por_id(self, id: int):
        return self.repositorio.obtener_producto_por_id(id)
        
    def Crear_producto(self, id: int, nombre: str, precio: float, stock_actual: int, stock_minimo: int, descripcion: str, categoria_id: int, proveedor_id: int):
        return self.repositorio.crear_producto(id, nombre, precio, stock_actual, stock_minimo, descripcion, categoria_id, proveedor_id)
    
    def Eliminar_producto(self, id: int):
        if not id:
            return {"message": "El ID del producto es obligatorio"}
        
        resultado = self.repositorio.eliminar_producto(id)
        return resultado
    
