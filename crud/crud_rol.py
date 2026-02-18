    '''
    Crud para los modelos de la paginacion .
    '''

import models.models_rol
import schemas.schema_rol
from sqlalchemy.orm import Session


def get_rol(db:Session, skip: int = 0, limit:int=10):

     '''
    Obtiene una lista de roles con paginación.
    '''
    return db.query(models.models_rol)ofset(skip)limit(limit).all()