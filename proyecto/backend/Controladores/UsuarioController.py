from fastapi import APIRouter, HTTPException
from Servicios.UsuarioService import UsuarioService

router = APIRouter(
prefix="/usuarios", tags=["Usuarios"])

usuario_service = UsuarioService()

#  Registrar usuario
@router.post("/registro")

def registrar_usuario(id_usuario: int, nombre_completo: str, username: str, password: str, rol: str):
    return usuario_service.Crear_usuario(id_usuario, nombre_completo, username, password, rol)

# Obtener perfil propio
@router.get("/{id_usuario}")

def ver_perfil(id_usuario: int):
    usuario = usuario_service.Ver_perfil(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario