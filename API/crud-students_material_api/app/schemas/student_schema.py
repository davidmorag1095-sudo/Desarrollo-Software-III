from pydantic import BaseModel, ConfigDict


class StudentSchema(BaseModel):
    carnet: str
    name: str
    age: int

    model_config = ConfigDict(from_attributes=True)

