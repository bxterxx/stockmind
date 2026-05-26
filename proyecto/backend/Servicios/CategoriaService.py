from proyecto.backend.Persistencia.Repositorios.CategoriaRepository import CategoriaRepository


class CategoriaService:
    def __init__(self):
        self.repositorio = CategoriaRepository()
        
    def crear_categoria(self, categoria_id: int, nombre: str):
        if not categoria_id or not nombre:
            return {"message": "El ID y el nombre de la categoría son obligatorios"}    
        id_creado = self.repositorio.Crear_categoria(nombre)
        
        if id_creado:
            return {"message": f"Categoría {nombre} creada correctamente con ID {id_creado}"}
        
    def eliminar_categoria(self, categoria_id: int):
        if not categoria_id:
            return {"message": "El ID de la categoría es obligatorio"}
        
        resultado = self.repositorio.Eliminar_categoria(categoria_id)
        return resultado
    
