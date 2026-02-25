"""
Crud para el modelo de Vehiculo.
"""

from sqlalchemy.orm import Session
from models.model_vehiculo import Vehiculo
from schemas.schema_vehiculo import VehiculoCreate

def get_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vehiculo).offset(skip).limit(limit).all()

def create_vehiculo(db: Session, vehiculo: VehiculoCreate):
    nuevo = Vehiculo(**vehiculo.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def delete_vehiculo(db: Session, au_id: int):
    vehiculo = db.query(Vehiculo).filter(Vehiculo.au_id == au_id).first()
    if vehiculo:
        db.delete(vehiculo)
        db.commit()
    return vehiculo