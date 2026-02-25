"""
Modelo Vehiculo para la base de datos.
"""

# pylint: disable=import-error
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from config.db import Base
from datetime import datetime


class Vehiculo(Base):
    """
    Representa la tabla tbb_vehiculo.
    """
    __tablename__ = "tbb_vehiculo"

    au_id = Column(Integer, primary_key=True, index=True)
    us_id = Column(Integer, ForeignKey("tbb_usuario.id"), nullable=False)

    au_placa = Column(String(15), nullable=False, unique=True)
    au_modelo = Column(String(45), nullable=False)
    au_serie = Column(String(45), nullable=False, unique=True)
    au_color = Column(String(45), nullable=True)
    au_tipo = Column(String(45), nullable=True)
    au_anio = Column(Integer, nullable=True)

    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_modificacion = Column(DateTime, nullable=True)