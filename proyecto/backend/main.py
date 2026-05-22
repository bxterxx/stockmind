from fastapi import FastAPI
from Controladores import  usuario_controller
from Controladores import movimiento_controller, producto_controller

app = FastAPI()

app.include_router(producto_controller.router)
app.include_router(movimiento_controller.router)
app.include_router(usuario_controller.router)