"""
Punto de entrada principal para la API del backend de Autolavado.
Configura la aplicación FastAPI, inicializa la base de datos y registra las rutas.
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback

# pylint: disable=import-error
import config.db

# pylint: disable=unused-import
import models.model_rols
import models.model_usuario
import models.model_servicio
import models.model_vehiculo
import models.model_servicio_vehiculo
# pylint: enable=unused-import

from routes.routes_rol import rol
from routes.routes_servicio import servicio
from routes.routes_servicio_vehiculo import servicios_vehiculo
from routes.routes_usuario import usuario
from routes.routes_vehiculo import vehiculo
# pylint: enable=import-error

app = FastAPI(
    title="Sistema de Autolavado CarWash API",
    description="""
API REST diseñada para la gestión integral de un sistema de autolavado.
Permite administrar clientes, vehículos, servicios, roles y usuarios,
optimizando los procesos operativos y el control de la información.
""",
    version="1.0.0"
)

# Manejador ANTES de los routers
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

# Crear tablas
models.model_rols.Base.metadata.create_all(bind=config.db.engine)

# Incluir routers
app.include_router(usuario)
app.include_router(rol)
app.include_router(vehiculo)
app.include_router(servicio)
app.include_router(servicios_vehiculo)

@app.get("/", tags=["Inicio"])
def read_root():
    """
    Ruta raíz para verificar que la API está levantada correctamente.
    """
    return {"mensaje": "Bienvenido a la API de Autolavado CarWash!"}