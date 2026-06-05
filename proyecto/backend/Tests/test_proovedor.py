import pytest
from unittest.mock import MagicMock
from Servicios.ProovedorService import ProovedorService

@pytest.fixture
def proveedor():
    proveedor_service = ProovedorService()
    proveedor_service.repositorio = MagicMock()
    return proveedor_service


def test_listar_proveedores_normal(proveedor):
    # DATOS
    proveedor.repositorio.listar_prooveedores.return_value = [
        {"id": 1, "nombre_empresa": "Distribuidora SAS", "telefono": "1234567"},
        {"id": 2, "nombre_empresa": "Lácteos del Norte", "telefono": "7654321"}
    ]
    
    # EJECUCIÓN
    resultado = proveedor.Listar_proveedores()
    
    # VALIDACIÓN
    assert len(resultado) == 2


def test_listar_proveedores_vacio(proveedor):
    # DATOS
    proveedor.repositorio.listar_prooveedores.return_value = []
    
    # EJECUCIÓN
    resultado = proveedor.Listar_proveedores()
    
    # VALIDACIÓN
    assert len(resultado) == 0


def test_crear_proveedor_exitoso(proveedor):
    # DATOS
    proveedor.repositorio.crear_proveedor.return_value = True
    
    # EJECUCIÓN
    resultado = proveedor.Crear_proveedor(id=1, nombre_empresa="Distribuidora SAS", telefono="1234567")
    
    # VALIDACIÓN
    assert resultado == {"message": "Proveedor Distribuidora SAS creado correctamente con ID 1"}


def test_crear_proveedor_faltan_campos(proveedor):
    # DATOS
    # EJECUCIÓN
    resultado = proveedor.Crear_proveedor(id=0, nombre_empresa="", telefono=None)
    
    # VALIDACIÓN
    assert resultado == {"message": "El ID y el nombre de la empresa son obligatorios"}


def test_eliminar_proveedor_exitoso(proveedor):
    # DATOS
    proveedor.repositorio.eliminar_proveedor.return_value = True
    
    # EJECUCIÓN
    resultado = proveedor.Eliminar_proveedor(id=1)
    
    # VALIDACIÓN
    assert resultado is True


def test_eliminar_proveedor_fallido(proveedor):
    # DATOS
    proveedor.repositorio.eliminar_proveedor.return_value = False
    
    # EJECUCIÓN
    resultado = proveedor.Eliminar_proveedor(id=999)
    
    # VALIDACIÓN
    assert resultado is False