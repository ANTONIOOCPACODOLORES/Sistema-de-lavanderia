"""
Rutas para la gestión de los servicios de vehículos
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db

from schemas.schema_servicio_vehiculo import (
    ServicioVehiculoCreate,
    ServicioVehiculoResponse,
)

from crud.crud_servicio_vehiculo import (
    get_servicio_vehiculo,
    get_servicio_vehiculo_by_id,
    create_servicio_vehiculo,
    update_servicio_vehiculo,
    delete_servicio_vehiculo,
)

servicios_vehiculo = APIRouter(
    prefix="/servicios-vehiculo",
    tags=["ServicioVehiculo"],
)

# ---------------------------
# GET /servicios-vehiculo/
# ---------------------------
@servicios_vehiculo.get(
    "/",
    response_model=List[ServicioVehiculoResponse],
)
def listar_servicios_vehiculo(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return get_servicio_vehiculo(db, skip, limit)


# ---------------------------
# GET /servicios-vehiculo/{id}
# ---------------------------
@servicios_vehiculo.get(
    "/{as_id}",
    response_model=ServicioVehiculoResponse,
)
def obtener_servicio_vehiculo(
    as_id: int,
    db: Session = Depends(get_db),
):
    servicio = get_servicio_vehiculo_by_id(db, as_id)
    if not servicio:
        raise HTTPException(
            status_code=404,
            detail="ServicioVehiculo no encontrado",
        )
    return servicio


# ---------------------------
# POST /servicios-vehiculo/
# ---------------------------
@servicios_vehiculo.post(
    "/",
    response_model=ServicioVehiculoResponse,
)
def crear_servicio_vehiculo(
    data: ServicioVehiculoCreate,
    db: Session = Depends(get_db),
):
    return create_servicio_vehiculo(db, data)


# ---------------------------
# PUT /servicios-vehiculo/{id}
# ---------------------------
@servicios_vehiculo.put(
    "/{as_id}",
    response_model=ServicioVehiculoResponse,
)
def actualizar_servicio_vehiculo(
    as_id: int,
    data: ServicioVehiculoCreate,
    db: Session = Depends(get_db),
):
    servicio = update_servicio_vehiculo(db, as_id, data)
    if not servicio:
        raise HTTPException(
            status_code=404,
            detail="ServicioVehiculo no encontrado",
        )
    return servicio


# ---------------------------
# DELETE /servicios-vehiculo/{id}
# ---------------------------
@servicios_vehiculo.delete("/{as_id}")
def eliminar_servicio_vehiculo(
    as_id: int,
    db: Session = Depends(get_db),
):
    servicio = delete_servicio_vehiculo(db, as_id)
    if not servicio:
        raise HTTPException(
            status_code=404,
            detail="ServicioVehiculo no encontrado",
        )
    return {"message": "ServicioVehiculo eliminado correctamente"}