from fastapi import APIRouter, HTTPException

from app.schemas.citas_schema import CitasSchema
from app.service.service_citas import ServiceCitas

router = APIRouter(prefix="/citas", tags=["Citas"])
service = ServiceCitas()


@router.post("/", response_model=CitasSchema)
def registrar_cita(cita: CitasSchema):
    try:
        return service.registrar_cita(
            cita.codigo_mascota,
            cita.fecha,
            cita.hora,
            cita.motivo,
            cita.estado
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{id}", response_model=CitasSchema)
def buscar_cita(id: int):
    cita = service.buscar_cita(id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita


@router.get("/", response_model=list[CitasSchema])
def listar_citas():
    return service.listar_citas()


@router.put("/{id}", response_model=CitasSchema)
def actualizar_cita(id: int, cita: CitasSchema):
    try:
        actualizada = service.actualizar_cita(
            id,
            cita.codigo_mascota,
            cita.fecha,
            cita.hora,
            cita.motivo,
            cita.estado
        )
        if not actualizada:
            raise HTTPException(status_code=404, detail="Cita no encontrada")
        return actualizada
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/{id}")
def eliminar_cita(id: int):
    eliminada = service.eliminar_cita(id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return {"message": "Cita eliminada"}

