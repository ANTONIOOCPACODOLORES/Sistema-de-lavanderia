# routes/routes_user.py
"""
Rutas para la gestión de Usuarios
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import config.db
import models.model_usuario
import crud.crud_usuario

# Importar directamente los schemas Pydantic
from schemas.schema_usuario import Usuario, UsuarioCreate, UsuarioUpdate

# Crear router
usuario = APIRouter()

# Crear las tablas si no existen
models.model_usuario.Base.metadata.create_all(bind=config.db.engine)

# Dependencia para la sesión de la base de datos
def get_db():
    """
    Función para obtener la sesión de la base de datos.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ====================== GET ======================
@usuario.get("/usuario/", response_model=List[Usuario], tags=["Usuario"])
async def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Obtener lista de usuarios con paginación.
    """
    return crud.crud_usuario.get_usuario(db=db, skip=skip, limit=limit)


@usuario.get("/usuario/{usuario_id}", response_model=Usuario, tags=["Usuario"])
async def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Obtener un usuario por ID.
    """
    db_usuario = crud.crud_usuario.get_usuario_by_id(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario


# ====================== POST ======================
@usuario.post("/usuario/", response_model=Usuario, tags=["Usuario"])
async def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Crear un nuevo usuario.
    """
    return crud.crud_usuario.create_usuario(db=db, usuario=usuario)


# ====================== PUT ======================
@usuario.put("/usuario/{usuario_id}", response_model=Usuario, tags=["Usuario"])
async def update_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    """
    Actualizar un usuario existente por ID.
    """
    db_usuario = crud.crud_usuario.get_usuario_by_id(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return crud.crud_usuario.update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)


# ====================== DELETE ======================
@usuario.delete("/usuario/{usuario_id}", response_model=dict, tags=["Usuario"])
async def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """
    Eliminar un usuario por ID.
    """
    db_usuario = crud.crud_usuario.get_usuario_by_id(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    crud.crud_usuario.delete_usuario(db=db, usuario_id=usuario_id)
    return {"message": f"Usuario {usuario_id} eliminado correctamente"}