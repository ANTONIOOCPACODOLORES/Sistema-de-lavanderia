"""
Rutas para la gestión de servicios
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import config.db
from models import model_servicio
from schemas import schema_servicio
from crud import crud_servicio

servicio = APIRouter()

# Crear tablas si no existen
model_servicio.Base.metadata.create_all(bind=config.db.engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para listar servicios
@servicio.get(
    "/servicios/", 
    response_model=List[schema_servicio.ServicioBase], 
    tags=["Servicio"]
)
async def read_servicio(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint para obtener una lista de servicios con paginación.
    """
    db_servicio = crud_servicio.get_servicio(db=db, skip=skip, limit=limit)
    return db_servicio
