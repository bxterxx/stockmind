from fastapi import FastAPI
from proyecto.backend.Controladores import  UsuarioController
from proyecto.backend.Controladores import ProductoController
from proyecto.backend.Controladores import MovimientoController

app = FastAPI()

app.include_router(ProductoController.router)
app.include_router(MovimientoController.router)
app.include_router(UsuarioController.router)