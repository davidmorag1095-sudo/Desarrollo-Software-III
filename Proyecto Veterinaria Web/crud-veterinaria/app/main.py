from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database_conexion import init_db
from app.controller.controller_citas_api import router as citas_router
from app.controller.controller_duenos_api import router as duenos_router
from app.controller.controller_login_api import router as login_router
from app.controller.controller_mascotas_api import router as mascotas_router
from app.controller.controller_reportes_api import router as reportes_router
from app.service.service_usuarios import ServiceUsuarios

app = FastAPI(title="Clínica Veterinaria API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()
ServiceUsuarios().crear_usuario_inicial()

app.include_router(login_router)
app.include_router(duenos_router)
app.include_router(mascotas_router)
app.include_router(citas_router)
app.include_router(reportes_router)


@app.get("/")
def inicio():
    return {"message": "API de la clínica veterinaria funcionando"}

