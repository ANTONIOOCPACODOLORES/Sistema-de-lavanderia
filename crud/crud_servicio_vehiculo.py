"""
CRUD para el modelo ServicioVehiculo
"""

from sqlalchemy.orm import Session
from models.model_servicio_vehiculo import ServicioVehiculo
from schemas.schema_servicio_vehiculo import (
    ServicioVehiculoCreate,
    ServicioVehiculoUpdate
)

# ---------------------------
# GET LIST
# ---------------------------
def get_servicio_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(ServicioVehiculo)
        .offset(skip)
        .limit(limit)
        .all()
    )

# ---------------------------
# GET BY ID
# ---------------------------
def get_servicio_vehiculo_by_id(db: Session, id: int):
    return (
        db.query(ServicioVehiculo)
        .filter(ServicioVehiculo.id == id)
        .first()
    )

# ---------------------------
# CREATE
# ---------------------------
def create_servicio_vehiculo(
    db: Session,
    data: ServicioVehiculoCreate
):
    nuevo = ServicioVehiculo(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# ---------------------------
# UPDATE
# ---------------------------
def update_servicio_vehiculo(
    db: Session,
    id: int,
    data: ServicioVehiculoUpdate
):
    servicio = get_servicio_vehiculo_by_id(db, id)
    if not servicio:
        return None

    for key, value in data.model_dump().items():
        setattr(servicio, key, value)

    db.commit()
    db.refresh(servicio)
    return servicio

# ---------------------------
# DELETE
# ---------------------------
def delete_servicio_vehiculo(db: Session, id: int):
    servicio = get_servicio_vehiculo_by_id(db, id)
    if not servicio:
        return None

    db.delete(servicio)
    db.commit()
    return servicio