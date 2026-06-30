from pydantic import BaseModel, ConfigDict


class DuenosSchema(BaseModel):
    id: int | None = None
    nombre: str
    telefono: str
    email: str

    model_config = ConfigDict(from_attributes=True)

