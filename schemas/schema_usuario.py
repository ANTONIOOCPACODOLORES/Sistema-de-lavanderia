# schemas/schema_usuario.py
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    rol_id: int
    nombre: str
    papellido: str
    sapellido: Optional[str] = None
    usuario: str
    password: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    estatus: Optional[bool] = True
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None

class UsuarioCreate(UsuarioBase):
    # Para creación, los campos de fecha se generan automáticamente
    pass

class UsuarioUpdate(BaseModel):
    rol_id: Optional[int]
    nombre: Optional[str]
    papellido: Optional[str]
    sapellido: Optional[str]
    usuario: Optional[str]
    password: Optional[str]
    direccion: Optional[str]
    telefono: Optional[str]
    correo: Optional[str]
    estatus: Optional[bool]

class Usuario(UsuarioBase):
    id: int

    model_config = {
        "from_attributes": True  # permite conversión ORM -> Pydantic
    }

class UsuarioLogin(BaseModel):
    correo: Optional[str] = None
    telefono: Optional[str] = None
    password: str