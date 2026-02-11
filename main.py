from fastapi import FastAPI
import routes.routes_rol  # Solo importa el archivo para que se ejecute

app = FastAPI(
    title="API de Roles",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}
