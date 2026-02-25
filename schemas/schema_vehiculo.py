"""
Esquemas Pydantic para Vehiculo.
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class VehiculoBase(BaseModel):
    au_placa: str
    au_modelo: str
    au_serie: str
    au_color: Optional[str] = None
    au_tipo: Optional[str] = None
    au_anio: Optional[int] = None


class VehiculoCreate(VehiculoBase):
    us_id: int


class VehiculoUpdate(BaseModel):
    au_modelo: Optional[str] = None
    au_color: Optional[str] = None
    au_tipo: Optional[str] = None
    au_anio: Optional[int] = None
    estatus: Optional[bool] = None
    fecha_modificacion: Optional[datetime] = None


class VehiculoResponse(VehiculoBase):
    au_id: int
    us_id: int
    estatus: bool
    fecha_registro: datetime
    fecha_modificacion: Optional[datetime]

    class Config:
        from_attributes = True