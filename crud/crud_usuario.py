"""
Módulo CRUD para la gestión del modelo de Usuario.
Contiene las operaciones de base de datos para crear, leer,
actualizar, eliminar y autenticar usuarios en el sistema.
"""
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.exc import UnknownHashError

# pylint: disable=import-error
from models import model_usuario
from schemas import schema_usuario
from models import model_rols  # ← AGREGA ESTA LÍNEA
from models import model_servicio  # ← AGREGA ESTA LÍNEA
from models import model_vehiculo  # ← AGREGA ESTA LÍNEA
from models import model_servicio_vehiculo  # ← AGREGA ESTA LÍNEA

# pylint: enable=import-error

# Configuración del encriptador usando el esquema argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def get_usuario(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model_usuario.Usuario).offset(skip).limit(limit).all()


def get_usuario_by_id(db: Session, usuario_id: int):
    return db.query(model_usuario.Usuario).filter(
        model_usuario.Usuario.id == usuario_id
    ).first()


def get_usuario_by_username(db: Session, usuario: str):
    return db.query(model_usuario.Usuario).filter(
        model_usuario.Usuario.usuario == usuario
    ).first()


def create_usuario(db: Session, usuario_in: schema_usuario.UsuarioCreate):
    """
    Crea un nuevo usuario en la base de datos, encriptando su contraseña.
    """
    try:
        password_plana = str(usuario_in.password).strip()
        hashed_password = pwd_context.hash(password_plana)

        db_usuario = model_usuario.Usuario(
            rol_id=usuario_in.rol_id,
            nombre=usuario_in.nombre,
            papellido=usuario_in.papellido,
            sapellido=usuario_in.sapellido,
            usuario=usuario_in.usuario,
            password=hashed_password,
            direccion=usuario_in.direccion,
            telefono=usuario_in.telefono,
            correo=usuario_in.correo,
            estatus=usuario_in.estatus
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except Exception as e:
        print(f"❌ ERROR EN CREATE_USUARIO: {type(e).__name__}: {e}")
        db.rollback()
        raise


def update_usuario(db: Session, usuario_id: int, usuario_in: schema_usuario.UsuarioUpdate):
    db_usuario = db.query(model_usuario.Usuario).filter(
        model_usuario.Usuario.id == usuario_id
    ).first()

    if db_usuario:
        update_data = usuario_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario


def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(model_usuario.Usuario).filter(
        model_usuario.Usuario.id == usuario_id
    ).first()

    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario


def authenticate_user(db: Session, login_id: str, contrasena: str):
    usuario_db = db.query(model_usuario.Usuario).filter(
        (model_usuario.Usuario.usuario == login_id) |
        (model_usuario.Usuario.correo == login_id) |
        (model_usuario.Usuario.telefono == login_id)
    ).first()

    if not usuario_db:
        return None

    try:
        if not pwd_context.verify(contrasena, usuario_db.password):
            return None
    except UnknownHashError:
        return None

    return usuario_db