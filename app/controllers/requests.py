from typing import List, Optional

from pydantic import BaseModel

from app.models import Address


class FarmerRequest(BaseModel):
    name: str
    cpf: Optional[str] = None
    cnpj: Optional[str] = None


class FarmRequest(BaseModel):
    name: str
    address: Address
    area_in_hec: float
    arable_area_in_hec: float
    vegetation_area_in_hec: float
    cultures: List[str] = []
