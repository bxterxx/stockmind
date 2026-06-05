from abc import ABC, abstractmethod


class CategoriaInterface(ABC):
    @abstractmethod
    def obtener_categorias(self):
        pass

    @abstractmethod
    def obtener_categoria_por_id(self, categoria_id: int):
        pass

    @abstractmethod
    def crear_categoria(self, categoria_id: int, nombre: str):
        pass

    @abstractmethod
    def eliminar_categoria(self, categoria_id: int):
        pass