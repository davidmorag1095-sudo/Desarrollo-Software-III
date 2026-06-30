from fastapi import APIRouter, HTTPException

from app.schemas.mascotas_schema import MascotasSchema
from app.service.service_mascotas import ServiceMascotas

router = APIRouter(prefix="/mascotas", tags=["Mascotas"])
service = ServiceMascotas()


@router.post("/", response_model=MascotasSchema)
def registrar_mascota(mascota: MascotasSchema):
    try:
        return service.registrar_mascota(
            mascota.codigo,
            mascota.nombre,
            mascota.especie,
            mascota.edad,
            mascota.dueno_id
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{codigo}", response_model=MascotasSchema)
def buscar_mascota(codigo: str):
    mascota = service.buscar_mascota(codigo)
    if not mascota:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.get("/", response_model=list[MascotasSchema])
def listar_mascotas():
    return service.listar_mascotas()


@router.put("/{codigo}", response_model=MascotasSchema)
def actualizar_mascota(codigo: str, mascota: MascotasSchema):
    try:
        actualizada = service.actualizar_mascota(
            codigo,
            mascota.nombre,
            mascota.especie,
            mascota.edad,
            mascota.dueno_id
        )
        if not actualizada:
            raise HTTPException(status_code=404, detail="Mascota no encontrada")
        return actualizada
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/{codigo}")
def eliminar_mascota(codigo: str):
    eliminada = service.eliminar_mascota(codigo)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return {"message": "Mascota eliminada"}

