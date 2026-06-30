from fastapi import APIRouter, HTTPException

from app.schemas.duenos_schema import DuenosSchema
from app.service.service_duenos import ServiceDuenos

router = APIRouter(prefix="/duenos", tags=["Dueños"])
service = ServiceDuenos()


@router.post("/", response_model=DuenosSchema)
def registrar_dueno(dueno: DuenosSchema):
    try:
        return service.registrar_dueno(dueno.nombre, dueno.telefono, dueno.email)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{id}", response_model=DuenosSchema)
def buscar_dueno(id: int):
    dueno = service.buscar_dueno(id)
    if not dueno:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return dueno


@router.get("/", response_model=list[DuenosSchema])
def listar_duenos(nombre: str | None = None):
    if nombre:
        return service.filtrar_duenos(nombre)
    return service.listar_duenos()


@router.put("/{id}", response_model=DuenosSchema)
def actualizar_dueno(id: int, dueno: DuenosSchema):
    try:
        actualizado = service.actualizar_dueno(id, dueno.nombre, dueno.telefono, dueno.email)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Dueño no encontrado")
        return actualizado
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/{id}")
def eliminar_dueno(id: int):
    try:
        eliminado = service.eliminar_dueno(id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Dueño no encontrado")
        return {"message": "Dueño eliminado"}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

