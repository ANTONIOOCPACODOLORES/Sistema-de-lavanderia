from fastapi import FastAPI
import config.db

# importar modelos para creación automática de tablas
import models.model_rols
import models.model_usuario
import models.model_servicio
import models.model_vehiculo
import models.model_servicio_vehiculo

# importar rutas (routers)
from routes.routes_rol import rol
from routes.routes_service import servicio
from routes.routes_service_vehicles import servicios_vehiculo
from routes.routes_user import usuario 

from routes.routes_vehicle import vehiculo

# crear la app
app = FastAPI(
    title="Sistema de Control de Autolavado",
    description="Sistema de creación y almacenamiento de información y ventas en un autolavado",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

# crear tablas en la base de datos al iniciar
models.model_rols.Base.metadata.create_all(bind=config.db.engine)
models.model_usuario.Base.metadata.create_all(bind=config.db.engine)
models.model_servicio.Base.metadata.create_all(bind=config.db.engine)
models.model_vehiculo.Base.metadata.create_all(bind=config.db.engine)
models.model_servicio_vehiculo.Base.metadata.create_all(bind=config.db.engine)

# incluir routers en la app
app.include_router(rol)
app.include_router(servicio)
app.include_router(servicios_vehiculo)
app.include_router(usuario)
app.include_router(vehiculo)