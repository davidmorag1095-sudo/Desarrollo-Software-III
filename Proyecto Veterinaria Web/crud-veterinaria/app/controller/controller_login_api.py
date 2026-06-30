from fastapi import APIRouter, HTTPException

from app.schemas.login_schema import LoginSchema
from app.service.service_usuarios import ServiceUsuarios

router = APIRouter(prefix="/login", tags=["Login"])
service = ServiceUsuarios()


@router.post("/")
def iniciar_sesion(login: LoginSchema):
    resultado = service.iniciar_sesion(login.usuario, login.clave)
    if not resultado:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    return resultado

