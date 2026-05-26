from fastapi import FastAPI
from Controladores import  CategoriaController, ProovedorController, UsuarioController
from Controladores import ProductoController
from Controladores import MovimientoController

app = FastAPI()

app.include_router(ProductoController.router)
app.include_router(MovimientoController.router)
app.include_router(UsuarioController.router)
app.include_router(CategoriaController.router)
app.include_router(ProovedorController.router)