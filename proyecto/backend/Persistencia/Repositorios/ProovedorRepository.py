from proyecto.backend.Entidades.Proovedor import Proveedor


class ProovedorRepository: 
    def __init__(self, db):
        self.db = db

    def crear_proveedor(self, id: int, nombre_empresa: str, telefono: str = None):
        nuevo_proveedor = Proveedor(id=id, nombre_empresa=nombre_empresa, telefono=telefono)
        self.db.add(nuevo_proveedor)
        self.db.commit()
        
    def obtener_catalogo_proveedor(self, id: int):
        proveedor = self.db.query(Proveedor).filter(Proveedor.id == id).first()
        if not proveedor:
            return {"message": f"Proveedor con ID {id} no encontrado"}
        return proveedor.productos