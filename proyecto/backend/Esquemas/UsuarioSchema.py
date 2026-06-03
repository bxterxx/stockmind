from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    username: str
    
class UsuarioCreate(UsuarioBase):
    username: str
    password: str  # Solo se pide al crear
    nombre_completo: str
    rol: str

class UsuarioOut(BaseModel):
    id_usuario: int
    nombre_completo: str
    username: str
    rol: str
    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    username: str
    password: str