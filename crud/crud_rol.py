"""
Archivo para operaciones CRUD de Roles
"""

from sqlalchemy.orm import Session
from datetime import datetime

from models.model_rols import Rol
from schemas.schema_rol import RolCreate, RolUpdate


def get_rol(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de roles con paginación.
    """
    return db.query(Rol).offset(skip).limit(limit).all()


def get_rol_by_id(db: Session, rol_id: int):
    """
    Obtiene un rol por ID.
    """
    return db.query(Rol).filter(Rol.id == rol_id).first()


def create_rol(db: Session, rol: RolCreate):
    """
    Crea un nuevo rol.
    """
    db_rol = Rol(
        nombre_rol=rol.nombre_rol,
        estatus=rol.estatus,
        fecha_registro=datetime.now(),
        fecha_modificacion=datetime.now()
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol


def update_rol(db: Session, rol_id: int, rol: RolUpdate):
    """
    Actualiza un rol existente.
    """
    db_rol = get_rol_by_id(db, rol_id)
    if not db_rol:
        return None

    if rol.nombre_rol is not None:
        db_rol.nombre_rol = rol.nombre_rol
    if rol.estatus is not None:
        db_rol.estatus = rol.estatus

    db_rol.fecha_modificacion = datetime.now()
    db.commit()
    db.refresh(db_rol)
    return db_rol


def delete_rol(db: Session, rol_id: int):
    """
    Elimina un rol.
    """
    db_rol = get_rol_by_id(db, rol_id)
    if not db_rol:
        return None

    db.delete(db_rol)
    db.commit()
    return db_rol