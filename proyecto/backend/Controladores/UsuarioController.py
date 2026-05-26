from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from proyecto.backend.Servicios import UsuarioService
from proyecto.backend.Esquemas.UsuarioSchema import UsuarioCreate, UsuarioOut, LoginSchema

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

#  Registrar usuario
@router.post("/registro", response_model=UsuarioOut)
def registrar_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService.create_user(db, data)

# Login (Simulado)
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = UsuarioService.authenticate(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return {"message": "Login exitoso", "user": user.username}

# Obtener perfil propio (Extra)
@router.get("/{id}", response_model=UsuarioOut)
def ver_perfil(id: int, db: Session = Depends(get_db)):
    user = UsuarioService.get_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    return user