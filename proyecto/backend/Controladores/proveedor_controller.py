from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from Servicios import proveedor_service
from Esquemas.proovedor_schema import ProveedorCreate, ProveedorOut

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

# Listar proveedores
@router.get("/", response_model=List[ProveedorOut])
def listar_proveedores(db: Session = Depends(get_db)):
    return proveedor_service.get_all(db)

# Crear proveedor
@router.post("/", response_model=ProveedorOut)
def crear_proveedor(data: ProveedorCreate, db: Session = Depends(get_db)):
    return proveedor_service.create(db, data)