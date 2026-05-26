from fastapi import APIRouter
from typing import List
from Servicios.ProovedorService import ProovedorService
from Esquemas.ProovedorSchema import ProveedorOut

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

# Listar proveedores
@router.get("/", response_model=List[ProveedorOut])

def listar_prooveedores(id: int, nombre_empresa: str, telefono: str):
    return ProovedorService.Listar_proveedores(id, nombre_empresa, telefono)

# Crear proveedor
@router.post("/", response_model=ProveedorOut)

def crear_prooveedor(id: int, nombre_empresa: str, telefono: str):
    return ProovedorService.Crear_proveedor(id, nombre_empresa, telefono)