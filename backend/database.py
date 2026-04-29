from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()

# Configuración desde variables de entorno
DB_ENGINE = os.getenv("DB_ENGINE", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "StockMind_Final")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Admin")

# Construir URL de conexión
DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Motor de base de datos
engine = create_engine(DATABASE_URL, echo=os.getenv("DEBUG", "False") == "True")

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session: # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Inicializar las tablas de la base de datos"""
    from Entity.usuario import Base as UsuarioBase
    from Entity.producto import Base as ProductoBase
    from Entity.movimiento import Base as MovimientoBase
    from Entity.proveedor import Base as ProveedorBase
    from Entity.categoria import Base as CategoriaBase
    
    # Importar Base de cada entidad y crear todas las tablas
    from sqlalchemy import MetaData
    
    # Usar la base de datos más reciente
    UsuarioBase.metadata.create_all(bind=engine)
    ProductoBase.metadata.create_all(bind=engine)
    MovimientoBase.metadata.create_all(bind=engine)
    ProveedorBase.metadata.create_all(bind=engine)
    CategoriaBase.metadata.create_all(bind=engine)