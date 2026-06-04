from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Controladores.ProductoController import router as router_productos
from Controladores.CategoriaController import router as router_categorias
from Controladores.ProovedorController import router as router_proveedores
from Controladores.MovimientoController import router as router_movimientos
from Controladores.UsuarioController import router as router_usuarios

app = FastAPI(
    title="StockMind API",
    description="Sistema de Gestión de Inventarios",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_productos)
app.include_router(router_categorias)
app.include_router(router_proveedores)
app.include_router(router_movimientos)
app.include_router(router_usuarios)
