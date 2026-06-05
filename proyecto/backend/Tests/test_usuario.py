import pytest
from unittest.mock import MagicMock
from Servicios.UsuarioService import UsuarioService

@pytest.fixture
def usuario():
    usuario_service = UsuarioService()
    usuario_service.repositorio = MagicMock()
    return usuario_service


def test_crear_usuario_exitoso(usuario):
    # DATOS
    usuario.repositorio.crear_usuario.return_value = True
    
    # EJECUCIÓN
    resultado = usuario.Crear_usuario(
        id_usuario=1, 
        nombre_completo="Andrés Botero", 
        username="abotero", 
        password="secure123", 
        rol="Administrador"
    )
    
    # VALIDACIÓN
    assert resultado == {
        "id_usuario": 1,
        "nombre_completo": "Andrés Botero",
        "username": "abotero",
        "rol": "Administrador"
    }


def test_crear_usuario_faltan_campos(usuario):
    # DATOS
    # EJECUCIÓN
    resultado = usuario.Crear_usuario(
        id_usuario=1, 
        nombre_completo="", 
        username="abotero", 
        password="", 
        rol=""
    )
    
    # VALIDACIÓN
    assert resultado == {"message": "El nombre completo, contraseña y rol son obligatorios"}


def test_ver_perfil_exitoso(usuario):
    # DATOS
    usuario.repositorio.ver_perfil.return_value = {
        "id_usuario": 1,
        "nombre_completo": "Andrés Botero",
        "username": "abotero",
        "rol": "Administrador"
    }
    
    # EJECUCIÓN
    resultado = usuario.Ver_perfil(id_usuario=1)
    
    # VALIDACIÓN
    assert resultado["username"] == "abotero"


def test_ver_perfil_no_encontrado(usuario):
    # DATOS
    usuario.repositorio.ver_perfil.return_value = None
    
    # EJECUCIÓN
    resultado = usuario.Ver_perfil(id_usuario=999)
    
    # VALIDACIÓN
    assert resultado == {"message": "Usuario con ID 999 no encontrado"}