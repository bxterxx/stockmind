from Persistencia.Repositorios.ProovedorRepository import ProovedorRepository


class ProovedorService:
    def __init__(self):
        self.repositorio = ProovedorRepository()
        
    def Listar_proveedores(self):
        proveedores = self.repositorio.listar_prooveedores()
        return proveedores
        
    def Crear_proveedor(self, id: int, nombre_empresa: str, telefono: str = None):
        if not id or not nombre_empresa:
            return {"message": "El ID y el nombre de la empresa son obligatorios"}
        
        self.repositorio.crear_proveedor(id, nombre_empresa, telefono)
        return {"message": f"Proveedor {nombre_empresa} creado correctamente con ID {id}"}
    
    def Eliminar_proveedor(self, id: int):
        success = self.repositorio.eliminar_proveedor(id)
        return success