# crud/crud_usuario.py
from sqlalchemy.orm import Session
from datetime import datetime
import models.model_usuario
from schemas.schema_usuario import UsuarioCreate, UsuarioUpdate

# ====================== GET ======================
def get_usuario(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.model_usuario.Usuario).offset(skip).limit(limit).all()

def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(models.model_usuario.Usuario).filter(models.model_usuario.Usuario.id == usuario_id).first()


# ====================== CREATE ======================
def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = models.model_usuario.Usuario(
        rol_id=usuario.rol_id,
        nombre=usuario.nombre,
        papellido=usuario.papellido,
        sapellido=usuario.sapellido,
        usuario=usuario.usuario,
        password=usuario.password,
        direccion=usuario.direccion,
        telefono=usuario.telefono,
        correo=usuario.correo,
        estatus=usuario.estatus if usuario.estatus is not None else True,
        fecha_registro=datetime.now(),
        fecha_modificacion=datetime.now()
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# ====================== UPDATE ======================
def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = get_usuario_by_id(db, usuario_id)
    if not db_usuario:
        return None

    for key, value in usuario.model_dump(exclude_unset=True).items():
        setattr(db_usuario, key, value)

    db_usuario.fecha_modificacion = datetime.now()
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# ====================== DELETE ======================
def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    if not db_usuario:
        return None

    db.delete(db_usuario)
    db.commit()
    return {"mensaje": f"Usuario con id {usuario_id} eliminado correctamente"}