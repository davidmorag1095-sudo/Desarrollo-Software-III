from pydantic import BaseModel, ConfigDict


class CitasSchema(BaseModel):
    id: int | None = None
    codigo_mascota: str
    fecha: str
    hora: str
    motivo: str
    estado: str

    model_config = ConfigDict(from_attributes=True)

