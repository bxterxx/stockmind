import pytest
import datetime
from unittest.mock import MagicMock
from Servicios.MovimientoService import MovimientoService

@pytest.fixture
def movimiento():
    movimiento_service = MovimientoService()
    movimiento_service.repositorio = MagicMock()
    return movimiento_service



def test_crear_movimiento_exitoso(movimiento):
    # DATOS
    movimiento.repositorio.crear_movimiento.return_value = True
    fecha_actual = datetime.date.today()
    
    # EJECUCIÓN
    resultado = movimiento.Crear_movimiento(id=1, producto_id=10, id_usuario=5, tipo="ENTRADA", cantidad=20, fecha=fecha_actual)
    
    # VALIDACIÓN 
    assert resultado == {"message": "Movimiento creado correctamente con ID 1"}


def test_crear_movimiento_error_repositorio(movimiento):
    # DATOS: 
    movimiento.repositorio.crear_movimiento.return_value = False
    fecha_actual = datetime.date.today()
    
    # EJECUCIÓN
    resultado = movimiento.Crear_movimiento(id=1, producto_id=10, id_usuario=5, tipo="ENTRADA", cantidad=20, fecha=fecha_actual)
    
    # VALIDACIÓN
    assert resultado == {"message": "Error al crear el movimiento"}


def test_crear_movimiento_faltan_campos(movimiento):
    # DATOS: parámetros vacíos o nulos 
    # EJECUCIÓN
    resultado = movimiento.Crear_movimiento(id=0, producto_id=0, id_usuario=0, tipo="", cantidad=None, fecha=None)
    
    # VALIDACIÓN
    assert resultado == {"message": "Todos los campos son obligatorios"}


def test_crear_movimiento_tipo_invalido(movimiento):
    # DATOS: 
    fecha_actual = datetime.date.today()
    
    # EJECUCIÓN Y VALIDACIÓN: 
    with pytest.raises(ValueError) as exc_info:
        movimiento.Crear_movimiento(id=1, producto_id=10, id_usuario=5, tipo="DAÑADO", cantidad=5, fecha=fecha_actual)
    
    assert str(exc_info.value) == "El tipo de movimiento debe ser 'ENTRADA' o 'SALIDA'"


def test_listar_movimientos_normal(movimiento):
    # DATOS
    movimiento.repositorio.listar_movimientos.return_value = [
        {"id": 1, "producto_id": 10, "tipo": "ENTRADA", "cantidad": 5},
        {"id": 2, "producto_id": 12, "tipo": "SALIDA", "cantidad": 2}
    ]
    
    # EJECUCIÓN
    resultado = movimiento.Listar_movimientos()
    
    # VALIDACIÓN
    assert len(resultado) == 2


def test_obtener_por_producto_normal(movimiento):
    # DATOS: 
    movimiento.repositorio.obtener_por_producto.return_value = [
        {"id": 1, "producto_id": 10, "tipo": "ENTRADA", "cantidad": 5}
    ]
    
    # EJECUCIÓN
    resultado = movimiento.Obtener_por_producto(10)
    
    # VALIDACIÓN
    assert len(resultado) == 1


def test_obtener_movimiento_id_exitoso(movimiento):
    # DATOS
    movimiento.repositorio.obtener_movimiento.return_value = {"id": 1, "producto_id": 10, "tipo": "ENTRADA"}
    
    # EJECUCIÓN
    resultado = movimiento.Obtener_movimiento(1)
    
    # VALIDACIÓN
    assert resultado == {"id": 1, "producto_id": 10, "tipo": "ENTRADA"}


def test_obtener_movimiento_id_no_encontrado(movimiento):
    # DATOS
    movimiento.repositorio.obtener_movimiento.return_value = None
    
    # EJECUCIÓN
    resultado = movimiento.Obtener_movimiento(999)
    
    # VALIDACIÓN
    assert resultado == {"message": "Movimiento con ID 999 no encontrado"}



def test_eliminar_movimiento_exitoso(movimiento):
    # DATOS
    movimiento.repositorio.eliminar_movimiento.return_value = True
    
    # EJECUCIÓN
    resultado = movimiento.Eliminar_movimiento(1)
    
    # VALIDACIÓN
    assert resultado is True