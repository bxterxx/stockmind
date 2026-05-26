from proyecto.backend.Persistencia.Repositorios.ProductoRepository import ProductoRepository


class ProductoService:
    def __init__(self):
        self.repositorio = ProductoRepository()
        
    def obtener_producto(self, id: int):
        producto = self.repositorio.obtener_producto(id)
        if not producto:
            return {"message": f"Producto con ID {id} no encontrado"}
        return producto
    
    def obtener_productos_por_id(self):
        productos = self.repositorio.obtener_productos()
        return productos
        
    def crear_producto(self, id: int, nombre: str, categoria_id: int, proveedor_id: int, precio: float, stock: int):
        if not id or not nombre or not categoria_id or not proveedor_id or precio is None or stock is None:
            return {"message": "Todos los campos son obligatorios"}
        
        producto_creado = self.repositorio.crear_producto(id, nombre, categoria_id, proveedor_id, precio, stock)
        
        if producto_creado:
            return {"message": f"Producto {nombre} creado correctamente con ID {id}"}
        
    def actualizar_producto(self, id: int, nombre: str, categoria_id: int, proveedor_id: int, precio: float, stock: int):
        if not id or not nombre or not categoria_id or not proveedor_id or precio is None or stock is None:
            return {"message": "Todos los campos son obligatorios"}
        
        producto_actualizado = self.repositorio.actualizar_producto(id, nombre, categoria_id, proveedor_id, precio, stock)
        
        if producto_actualizado:
            return {"message": f"Producto {nombre} actualizado correctamente con ID {id}"}
    
    def eliminar_producto(self, id: int):
        if not id:
            return {"message": "El ID del producto es obligatorio"}
        
        resultado = self.repositorio.eliminar_producto(id)
        return resultado
    
    
    def buscar_productos_por_nombre(self, termino: str):
        if not termino:
            return {"message": "El término de búsqueda es obligatorio"}
        
        productos_encontrados = self.repositorio.buscar_productos_por_nombre(termino)
        return productos_encontrados
    
    def productos_bajo_stock(self, limite: int):
        if limite is None:
            return {"message": "El límite de stock es obligatorio"}
        
        productos_bajo_stock = self.repositorio.productos_bajo_stock(limite)
        return productos_bajo_stock
    
    def calcular_valor_total_stock(self):
        valor_total = self.repositorio.calcular_valor_total_stock()
        return {"valor_total_stock": valor_total}
    
