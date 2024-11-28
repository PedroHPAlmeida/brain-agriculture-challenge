from typing import List

from pydantic import BaseModel

from app.models import Address


class FarmerRequest(BaseModel):
    name: str
    cpf: str | None = None
    cnpj: str | None = None


class FarmRequest:
    name: str
    address: Address
    area_in_hec: float
    arable_area_in_hec: float
    vegetation_area_in_hec: float
    cultures: List[str] = []
