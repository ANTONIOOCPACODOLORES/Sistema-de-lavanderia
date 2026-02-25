"""
Rutas para la gestión de Vehiculos
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db
from schemas.schema_vehiculo import VehiculoCreate, VehiculoResponse
from crud.crud_vehiculo import get_vehiculo, create_vehiculo, delete_vehiculo

vehiculo = APIRouter(prefix="/vehiculos", tags=["Vehiculo"])


@vehiculo.get("/", response_model=List[VehiculoResponse])
def listar_vehiculos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_vehiculo(db, skip, limit)


@vehiculo.post("/", response_model=VehiculoResponse)
def crear_vehiculo_endpoint(vehiculo_data: VehiculoCreate, db: Session = Depends(get_db)):
    return create_vehiculo(db, vehiculo_data)


@vehiculo.delete("/{au_id}")
def eliminar_vehiculo(au_id: int, db: Session = Depends(get_db)):
    vehiculo = delete_vehiculo(db, au_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return {"message": "Vehículo eliminado correctamente"}