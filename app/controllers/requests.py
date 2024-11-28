from pydantic import BaseModel


class FarmerRequest(BaseModel):
    name: str
    cpf: str | None = None
    cnpj: str | None = None
