"""
Esquemas Pydantic para Rol.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class RolBase(BaseModel):
    """
    Esquema base de Rol.
    """
    nombre_rol: str
    estatus: bool


class RolCreate(RolBase):
    """
    Esquema para crear rol.
    """
    pass


class RolUpdate(BaseModel):
    """
    Esquema para actualizar rol.
    """
    nombre_rol: Optional[str] = None
    estatus: Optional[bool] = None


class Rol(RolBase):
    """
    Esquema de respuesta de rol.
    """
    id: int
    fecha_registro: datetime
    fecha_modificacion: datetime

    class Config:
        orm_mode = True