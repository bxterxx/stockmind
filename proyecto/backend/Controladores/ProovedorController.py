from fastapi import APIRouter, HTTPException
from typing import List
from Servicios.ProovedorService import ProovedorService

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])
proovedor_service = ProovedorService()

# Listar proveedores
@router.get("/")

def listar_prooveedores():
    return proovedor_service.Listar_proveedores()

# Crear proveedor
@router.post("/")

def crear_prooveedor(id: int, nombre_empresa: str, telefono: str):
    return proovedor_service.Crear_proveedor(id, nombre_empresa, telefono)

# Eliminar proveedor
@router.delete("/{id}")
def eliminar_proveedor(id: int):
    success = proovedor_service.Eliminar_proveedor(id)
    if not success:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return {"message": "Proveedor eliminado exitosamente"}