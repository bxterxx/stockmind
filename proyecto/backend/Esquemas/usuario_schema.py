from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str  # Solo se pide al crear

class UsuarioOut(UsuarioBase):
    id: int
    # No se incluye el password
    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    username: str
    password: str