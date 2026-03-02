"""
Módulo CRUD para Vehículo.
Contiene las operaciones de Crear, Leer, Actualizar y Eliminar
registros de la tabla vehículos.
"""

from sqlalchemy.orm import Session

# Importamos el modelo Vehiculo (NO se redefine aquí)
# pylint: disable=import-error
from models.model_vehiculo import Vehiculo
# pylint: enable=import-error


# =========================
# CREATE
# =========================
def crear_vehiculo(db: Session, vehiculo: Vehiculo):
    """
    Crea un nuevo vehículo en la base de datos.
    """
    db.add(vehiculo)
    db.commit()
    db.refresh(vehiculo)
    return vehiculo


# =========================
# READ
# =========================
def obtener_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtiene la lista de vehículos.
    """
    return db.query(Vehiculo).offset(skip).limit(limit).all()


def obtener_vehiculo_por_id(db: Session, vehiculo_id: int):
    """
    Obtiene un vehículo por su ID.
    """
    return db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()


# =========================
# UPDATE
# =========================
def actualizar_vehiculo(db: Session, vehiculo_id: int, datos: dict):
    """
    Actualiza un vehículo existente.
    """
    vehiculo = obtener_vehiculo_por_id(db, vehiculo_id)

    if not vehiculo:
        return None

    for campo, valor in datos.items():
        setattr(vehiculo, campo, valor)

    db.commit()
    db.refresh(vehiculo)
    return vehiculo


# =========================
# DELETE
# =========================
def eliminar_vehiculo(db: Session, vehiculo_id: int):
    """
    Elimina un vehículo por su ID.
    """
    vehiculo = obtener_vehiculo_por_id(db, vehiculo_id)

    if not vehiculo:
        return None

    db.delete(vehiculo)
    db.commit()
    return vehiculo