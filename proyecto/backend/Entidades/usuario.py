from sqlalchemy import Column, Integer, String

class Usuario:
    __tablename__ = "Usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) # Nunca guardar en texto plano
    rol = Column(String, default="empleado") # admin o empleado