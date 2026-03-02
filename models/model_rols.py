"""
Módulo del modelo Rol para la base de datos.
Define la estructura de la tabla tbc_roles.
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# Desactivamos advertencias de importación para módulos locales
# pylint: disable=import-error
from config.db import Base
# pylint: enable=import-error


# Desactivamos la advertencia de "muy pocos métodos públicos"
# porque los modelos ORM representan tablas, no lógica de negocio.
# pylint: disable=too-few-public-methods
class Rol(Base):
    """
    Representa la tabla 'tbc_roles' en la base de datos.
    Contiene la definición de los diferentes roles del sistema.
    """

    __tablename__ = "tbc_roles"

    # Identificador único del rol
    id = Column(Integer, primary_key=True, index=True)

    # Nombre del rol (ej. Admin, Usuario, Cliente)
    nombre_rol = Column(String(60), nullable=False, unique=True)

    # Estatus del rol (activo / inactivo)
    estatus = Column(Boolean, default=True)

    # Fecha de creación del registro
    fecha_registro = Column(DateTime, default=func.now())

    # Fecha de última modificación del registro
    fecha_modificacion = Column(DateTime, onupdate=func.now())

    # Relación con la tabla usuarios
    usuarios = relationship("Usuario", back_populates="rol")
# pylint: enable=too-few-public-methods