"""Archivo para operaciones CRUD de Roles"""

import models.model_rols
import schemas.schema_rol
from sqlalchemy.orm import Session


def get_rol(db:Session, skip: int = 0, limit:int=10):

    """
    Obtiene una lista de roles con paginación.
    """
    
    return db.query(models.model_rols.Rol).offset(skip).limit(limit).all()
