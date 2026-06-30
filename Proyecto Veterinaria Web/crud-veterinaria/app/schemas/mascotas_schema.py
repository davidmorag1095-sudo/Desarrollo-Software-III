from pydantic import BaseModel, ConfigDict


class MascotasSchema(BaseModel):
    codigo: str
    nombre: str
    especie: str
    edad: int
    dueno_id: int

    model_config = ConfigDict(from_attributes=True)

