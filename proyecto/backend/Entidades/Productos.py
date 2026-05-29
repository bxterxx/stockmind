from sqlalchemy import Column, Float, ForeignKey, Integer, String


class producto:
    __tablename__ = "Productos"
    
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio_venta = Column(Float)
    stock_actual = Column(Integer)
    stock_minimo = Column(Integer)
    descripcion = Column(String)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    prooveedor_id = Column(Integer, ForeignKey("proveedores.id"))