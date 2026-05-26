from Persistencia.Repositorios.ProductoRepository import ProductoRepository


class ProductoService:
    def __init__(self):
        self.repositorio = ProductoRepository()
        
    def Obtener_productos(self, id: int):
        producto = self.repositorio.obtener_productos(id)
        if not producto:
            return {"message": f"Producto con ID {id} no encontrado"}
        return producto
    
    def Obtener_productos_por_id(self, categoria_id: int = None, proveedor_id: int = None):
        productos = self.repositorio.obtener_producto_por_id(categoria_id, proveedor_id)
        return productos
        
    def Crear_producto(self, id: int, nombre: str, categoria_id: int, proveedor_id: int, precio: float, stock: int):
        if not id or not nombre or not categoria_id or not proveedor_id or precio is None or stock is None:
            return {"message": "Todos los campos son obligatorios"}
        
        producto_creado = self.repositorio.crear_producto(id, nombre, categoria_id, proveedor_id, precio, stock)
        
        if producto_creado:
            return {"message": f"Producto {nombre} creado correctamente con ID {id}"}
    
    def Eliminar_producto(self, id: int):
        if not id:
            return {"message": "El ID del producto es obligatorio"}
        
        resultado = self.repositorio.eliminar_producto(id)
        return resultado
    
