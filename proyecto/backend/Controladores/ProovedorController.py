from fastapi import APIRouter
from typing import List
from Servicios.ProovedorService import ProovedorService
from Esquemas.ProovedorSchema import ProveedorOut

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])
proovedor_service = ProovedorService()

# Listar proveedores
@router.get("/", response_model=List[ProveedorOut])

def listar_prooveedores():
    return proovedor_service.Listar_proveedores()

# Crear proveedor
@router.post("/", response_model=None)

def crear_prooveedor(id: int, nombre_empresa: str, telefono: str):
    return proovedor_service.Crear_proveedor(id, nombre_empresa, telefono)