from typing import optional
from pydantic import BaseModel
'''
Docstring for schemas.schemas_rol
'''
from datetime import datetime

class UserBase(BaseModel):
    '''clase para modelar la tabla rols'''
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    correo_electronico: str 
    direccion: str
    contraseña: str
    telefono_celular: str
    estatus= bool
    fecha_actualizacion: datetime
    fecha_registro: datetime

#pylint: disable=tool-few-public-,unecessary-pass
class Rolcreate(RolBase):
    '''clase para crear un rol en la tabla rols'''
    pass
#pylint: disable=tool-few-public-methods
class RolUpdate (RolBase):
    '''clase para actualizar un rol basado en la tabla rols'''
    pass

class Rol (RolBase):
    '''clase para realizar operaciones por ID en la tabla rol'''
    id:int
    class config:
        '''utiliza un orm para ejecutar las funcionalidades'''
        orm_mode:True

class UserLogin(BaseModel):
    correo:optional{str} = None
    telefono:optional{str}=None