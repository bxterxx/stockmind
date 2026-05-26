from fastapi import APIRouter, HTTPException
from Servicios.UsuarioService import UsuarioService
from Esquemas.UsuarioSchema import  UsuarioOut, LoginSchema

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

#  Registrar usuario
@router.post("/registro", response_model=UsuarioOut)

def registrar_usuario(id: int, nombre_completo: str, username: str, password: str, rol: str):
    return UsuarioService.Crear_usuario(id, nombre_completo, username, password, rol)

# Login (Simulado)
@router.post("/login")

def login(id: int, username: str, password: str):
    user = UsuarioService.Login(id, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Login exitoso", "usuario": user}

# Obtener perfil propio (Extra)
@router.get("/{id}", response_model=UsuarioOut)

def ver_perfil(id: int):
    user = UsuarioService.Ver_perfil(id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user