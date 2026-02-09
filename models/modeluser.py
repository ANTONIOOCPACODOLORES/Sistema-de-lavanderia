from sqlalchemy import column
from sqlalchemy.orm
#pylint: disable=import.error
from config import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime


class User(Base):
    __tablename__ = "the_users"

    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey('the_rols.id'))
    nombre = Column(String(100), nullable=False)
    primer_apellido = Column(String(100), nullable=False)
    segundo_apellido = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    telefono_celular = Column(String(20))




    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    rol_id = Column(Integer, ForeignKey("the_roles.id"), nullable=False)

    rol=relationship("Rol",back_populates="usuarios" )

    