from fastapi import APIRouter

from app.service.service_citas import ServiceCitas
from app.service.service_mascotas import ServiceMascotas

router = APIRouter(prefix="/reportes", tags=["Reportes"])
service_mascotas = ServiceMascotas()
service_citas = ServiceCitas()


@router.get("/mascotas-por-especie")
def mascotas_por_especie():
    return service_mascotas.reporte_por_especie()


@router.get("/citas-por-estado")
def citas_por_estado():
    return service_citas.reporte_por_estado()

