from pydantic import BaseModel


class LoginSchema(BaseModel):
    usuario: str
    clave: str

