"""
Esquemas Pydantic para ServicioVehiculo.
"""

from datetime import datetime, time
from pydantic import BaseModel
from typing import Optional

# pylint: disable=too-few-public-methods
class ServicioVehiculoBase(BaseModel):
    """
    Esquema base de ServicioVehiculo.
    """
    au_id: int
    cajero_id: int
    operativo_id: int
    se_id: int
    as_fecha: Optional[datetime] = None
    as_hora: Optional[time] = None
    as_estatus: str
    as_estado: bool
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class ServicioVehiculoCreate(ServicioVehiculoBase):
    """
    Esquema para crear servicio de vehiculo.
    """
    pass


class ServicioVehiculoResponse(ServicioVehiculoBase):
    """
    Esquema de respuesta de servicio de vehiculo.
    """
    as_id: int

    class Config:
        # ✅ Pydantic v2
        from_attributes = True