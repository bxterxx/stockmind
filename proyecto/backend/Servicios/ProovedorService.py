from proyecto.backend.Persistencia.Repositorios.ProovedorRepository import ProovedorRepository


class ProovedorService:
    def __init__(self):
        self.repositorio = ProovedorRepository()
        
    def crear_proveedor(self, id: int, nombre_empresa: str, telefono: str = None):
        if not id or not nombre_empresa:
            return {"message": "El ID y el nombre de la empresa son obligatorios"}
        
        self.repositorio.crear_proveedor(id, nombre_empresa, telefono)
        return {"message": f"Proveedor {nombre_empresa} creado correctamente con ID {id}"}
    
    def obtener_catalogo_proveedor(self, id: int):
        catalogo = self.repositorio.obtener_catalogo_proveedor(id)
        if isinstance(catalogo, dict) and "message" in catalogo:
            return catalogo 
        return catalogo 