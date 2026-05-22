from sqlalchemy.orm import Session
from Entidades.usuario import Usuario
from fastapi import HTTPException
import hashlib # Ejemplo simple de hash (usa Passlib en proyecto real)

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario(db: Session, user_data):
    #  Verificar si el username o email ya existen
    if db.query(Usuario).filter(Usuario.username == user_data.username).first():
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está tomado")
    
    # Cifrar contraseña 
    hashed = hash_password(user_data.password)
    
    nuevo_usuario = Usuario(
        username=user_data.username,
        email=user_data.email,
        password=hashed,
        rol=user_data.rol or "empleado"
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def autenticar(db: Session, username, password):
    user = db.query(Usuario).filter(Usuario.username == username).first()
    if not user or user.password != hash_password(password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user