import pytest
from unittest.mock import MagicMock
from Servicios.ProductoService import ProductoService

@pytest.fixture
def producto():
    producto_service = ProductoService()
    producto_service.repositorio = MagicMock()
    return producto_service


def test_obtener_productos_normal(producto):
    # DATOS
    producto.repositorio.obtener_productos.return_value = [
        {"id": 1, "nombre": "Arroz 1kg", "precio": 4500.0, "stock_actual": 50},
        {"id": 2, "nombre": "Aceite 1L", "precio": 12000.0, "stock_actual": 20}
    ]
    
    # EJECUCIÓN
    resultado = producto.Obtener_productos()
    
    # VALIDACIÓN
    assert len(resultado) == 2


def test_obtener_productos_vacio(producto):
    # DATOS
    producto.repositorio.obtener_productos.return_value = []
    
    # EJECUCIÓN
    resultado = producto.Obtener_productos()
    
    # VALIDACIÓN
    assert len(resultado) == 0


def test_obtener_productos_por_id_exitoso(producto):
    # DATOS
    producto.repositorio.obtener_producto_por_id.return_value = {
        "id": 1, 
        "nombre": "Arroz 1kg", 
        "precio": 4500.0
    }
    
    # EJECUCIÓN
    resultado = producto.Obtener_productos_por_id(1)
    
    # VALIDACIÓN
    assert resultado["nombre"] == "Arroz 1kg"


def test_obtener_productos_por_id_no_encontrado(producto):
    # DATOS
    producto.repositorio.obtener_producto_por_id.return_value = None
    
    # EJECUCIÓN
    resultado = producto.Obtener_productos_por_id(999)
    
    # VALIDACIÓN
    assert resultado is None


def test_crear_producto_exitoso(producto):
    # DATOS
    producto.repositorio.crear_producto.return_value = True
    
    # EJECUCIÓN
    resultado = producto.Crear_producto(
        id=1, 
        nombre="Leche 1L", 
        precio=3800.0, 
        stock_actual=100, 
        stock_minimo=10, 
        descripcion="Leche entera pasteurizada", 
        categoria_id=2, 
        proveedor_id=3
    )
    
    # VALIDACIÓN
    assert resultado is True


def test_eliminar_producto_exitoso(producto):
    # DATOS
    producto.repositorio.eliminar_producto.return_value = "Producto eliminado exitosamente"
    
    # EJECUCIÓN
    resultado = producto.Eliminar_producto(id=1)
    
    # VALIDACIÓN
    assert resultado == "Producto eliminado exitosamente"


def test_eliminar_producto_id_invalido(producto):
    # DATOS
    # EJECUCIÓN
    resultado = producto.Eliminar_producto(id=0)
    
    # VALIDACIÓN
    assert resultado == {"message": "El ID del producto es obligatorio"}