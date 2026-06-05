import pytest
from unittest.mock import MagicMock
from Servicios.CategoriaService import CategoriaService

@pytest.fixture
def categoria():
    categoria_service = CategoriaService()
    categoria_service.repositorio = MagicMock()
    return categoria_service


def test_obtener_categorias_normal(categoria):
    # DATOS
    categoria.repositorio.obtener_categorias.return_value = [
        {"id": 1, "nombre": "Grano"},
        {"id": 2, "nombre": "Bebidas"}
    ]
    
    # EJECUCIÓN
    categorias = categoria.Obtener_categorias()
    
    # VALIDACIÓN
    assert len(categorias) == 2


def test_obtener_categorias_vacio(categoria):
    # DATOS
    categoria.repositorio.obtener_categorias.return_value = []
    
    # EJECUCIÓN
    categoriasVacias = categoria.Obtener_categorias()
    
    # VALIDACIÓN
    assert len(categoriasVacias) == 0



def test_obtener_categoria_por_id_exitoso(categoria):
    # DATOS
    categoria.repositorio.obtener_categoria_por_id.return_value = {"id": 1, "nombre": "Grano"}
    
    # EJECUCIÓN
    resultado = categoria.Obtener_categoria_por_id(1)
    
    # VALIDACIÓN
    assert resultado == {"id": 1, "nombre": "Grano"}


def test_obtener_categoria_por_id_no_encontrada(categoria):
    # DATOS: 
    categoria.repositorio.obtener_categoria_por_id.return_value = None
    
    # EJECUCIÓN
    resultado = categoria.Obtener_categoria_por_id(999)
    
    # VALIDACIÓN: 
    assert resultado == {"message": "Categoría con ID 999 no encontrada"}



def test_crear_categoria_exitoso(categoria):
    # DATOS: 
    categoria.repositorio.crear_categoria.return_value = 3
    
    # EJECUCIÓN
    resultado = categoria.Crear_categoria(categoria_id=3, nombre="Lácteos")
    
    # VALIDACIÓN: 
    assert resultado == {
        "message": "Categoría Lácteos creada correctamente",
        "id": 3,
        "nombre": "Lácteos"
    }
    categoria.repositorio.crear_categoria.assert_called_once_with(3, "Lácteos")


def test_crear_categoria_faltan_datos(categoria):
    # DATOS: ID o nombre evaluado en falso 
    # EJECUCIÓN
    resultado = categoria.Crear_categoria(categoria_id=0, nombre="")
    
    # VALIDACIÓN: 
    assert resultado == {"message": "El ID y el nombre de la categoría son obligatorios"}
    categoria.repositorio.crear_categoria.assert_not_called()



def test_eliminar_categoria_exitoso(categoria):
    # DATOS: 
    categoria.repositorio.eliminar_categoria.return_value = True
    
    # EJECUCIÓN
    resultado = categoria.Eliminar_categoria(categoria_id=1)
    
    # VALIDACIÓN:
    assert resultado == "Categoría eliminada exitosamente"
    categoria.repositorio.eliminar_categoria.assert_called_once_with(1)


def test_eliminar_categoria_id_invalido(categoria):
    # DATOS: ID evaluado en falso 
    # EJECUCIÓN
    resultado = categoria.Eliminar_categoria(categoria_id=0)
    
    # VALIDACIÓN
    assert resultado == {"message": "El ID de la categoría es obligatorio"}
    categoria.repositorio.eliminar_categoria.assert_not_called()