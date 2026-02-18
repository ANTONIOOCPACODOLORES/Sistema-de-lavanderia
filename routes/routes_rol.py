"""
Rutas para la gestión de roles
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import config.db
from models import model_rols
from schemas import schema_rol
from crud import crud_rol

rol = APIRouter()

# Crear tablas si no existen
model_rols.Base.metadata.create_all(bind=config.db.engine, checkfirst=True)

# Función para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar roles
@rol.get(
    "/rol/", 
    response_model=List[schema_rol.Rol], 
    tags=["Rol"]
)
async def read_rol(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint para obtener una lista de roles con paginación.
    """
    db_rol = crud_rol.get_rol(db=db, skip=skip, limit=limit)
    return db_rol
