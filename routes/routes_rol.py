"""
Rutas para la gestión de roles
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import config.db
from models import model_rols
from schemas.schema_rol import Rol, RolCreate, RolUpdate
from crud import crud_rol

rol = APIRouter(
    prefix="/rol",
    tags=["Rol"]
)

# Crear tablas si no existen
model_rols.Base.metadata.create_all(
    bind=config.db.engine,
    checkfirst=True
)

# Dependencia DB
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# GET /rol/
# -------------------------
@rol.get("/", response_model=List[Rol])
def listar_roles(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud_rol.get_rol(db, skip, limit)


# -------------------------
# GET /rol/{id}
# -------------------------
@rol.get("/{rol_id}", response_model=Rol)
def obtener_rol(
    rol_id: int,
    db: Session = Depends(get_db)
):
    rol_db = crud_rol.get_rol_by_id(db, rol_id)
    if not rol_db:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol_db


# -------------------------
# POST /rol/
# -------------------------
@rol.post("/", response_model=Rol)
def crear_rol(
    rol_data: RolCreate,
    db: Session = Depends(get_db)
):
    return crud_rol.create_rol(db, rol_data)


# -------------------------
# PUT /rol/{id}
# -------------------------
@rol.put("/{rol_id}", response_model=Rol)
def actualizar_rol(
    rol_id: int,
    rol_data: RolUpdate,
    db: Session = Depends(get_db)
):
    rol_actualizado = crud_rol.update_rol(db, rol_id, rol_data)
    if not rol_actualizado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol_actualizado


# -------------------------
# DELETE /rol/{id}
# -------------------------
@rol.delete("/{rol_id}")
def eliminar_rol(
    rol_id: int,
    db: Session = Depends(get_db)
):
    rol_eliminado = crud_rol.delete_rol(db, rol_id)
    if not rol_eliminado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"message": "Rol eliminado correctamente"}