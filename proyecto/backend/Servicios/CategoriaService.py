from Persistencia.Repositorios.CategoriaRepository import CategoriaRepository


class CategoriaService:
    def __init__(self):
        self.repositorio = CategoriaRepository()
        
    def Obtener_categorias(self):
        categorias = self.repositorio.obtener_categorias()
        return categorias
    
    def Obtener_categoria_por_id(self, categoria_id: int):
        categoria = self.repositorio.obtener_categoria_por_id(categoria_id)
        if categoria:
            return categoria
        return {"message": f"Categoría con ID {categoria_id} no encontrada"}
        
    def Crear_categoria(self, categoria_id: int, nombre: str):
        if not categoria_id or not nombre:
            return {"message": "El ID y el nombre de la categoría son obligatorios"}    
        id_creado = self.repositorio.crear_categoria(categoria_id, nombre)
        
        if id_creado:
            return {"message": f"Categoría {nombre} creada correctamente con ID {id_creado}"}
        
    def Eliminar_categoria(self, categoria_id: int):
        if not categoria_id:
            return {"message": "El ID de la categoría es obligatorio"}
        
        resultado = self.repositorio.eliminar_categoria(categoria_id)
        return resultado
    
