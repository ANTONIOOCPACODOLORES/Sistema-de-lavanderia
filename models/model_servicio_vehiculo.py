"""
Modelo ServicioVehiculo para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    ForeignKey,
    DateTime,
    Time,
    Enum
)
from sqlalchemy.sql import func
from enum import Enum as PyEnum

from config.db import Base


class Solicitud(PyEnum):
    """
    Enum para definir los estados de la solicitud de servicio.
    """
    Programada = "Programada"
    Proceso = "Proceso"
    Realizada = "Realizada"
    Cancelada = "Cancelada"


class ServicioVehiculo(Base):
    """
    Representa la tabla tbd_servicio_vehiculo.
    """
    __tablename__ = "tbd_servicio_vehiculo"

    as_id = Column(Integer, primary_key=True, index=True)

    au_id = Column(
        Integer,
        ForeignKey("tbb_vehiculo.au_id"),
        nullable=False
    )

    cajero_id = Column(
        Integer,
        ForeignKey("tbb_usuario.id"),
        nullable=False
    )

    operativo_id = Column(
        Integer,
        ForeignKey("tbb_usuario.id"),
        nullable=False
    )

    se_id = Column(
        Integer,
        ForeignKey("tbc_servicio.se_id"),
        nullable=False
    )

    as_fecha = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    as_hora = Column(
    DateTime,
    server_default=func.now(),
    nullable=False
    )

    as_estatus = Column(
        Enum(Solicitud, name="estatus_solicitud"),
        default=Solicitud.Programada,
        nullable=False
    )

    as_estado = Column(
        Boolean,
        default=True,
        nullable=False
    )

    fecha_registro = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    fecha_modificacion = Column(
        DateTime,
        onupdate=func.now(),
        nullable=True
    )