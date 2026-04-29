from sqlalchemy.orm import Session
from Entity.proveedor import Proveedor
from fastapi import HTTPException

def crear_proveedor(db: Session, prov_data):
    # Validar que el teléfono sea único si se proporciona
    if prov_data.telefono:
        existe = db.query(Proveedor).filter(Proveedor.telefono == prov_data.telefono).first()
        if existe:
            raise HTTPException(status_code=400, detail="El teléfono del proveedor ya está registrado")

    nuevo_prov = Proveedor(**prov_data.dict())
    db.add(nuevo_prov)
    db.commit()
    db.refresh(nuevo_prov)
    return nuevo_prov

def obtener_catalogo_proveedor(db: Session, prov_id: int):
    prov = db.query(Proveedor).filter(Proveedor.id == prov_id).first()
    if not prov:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return prov.productos 