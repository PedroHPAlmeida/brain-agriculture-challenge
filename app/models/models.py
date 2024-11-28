from typing import List
from uuid import uuid4

from pydantic import BaseModel, field_validator


class Farmer(BaseModel):
    id: str = uuid4().hex
    name: str
    cpf: str | None = None
    cnpj: str | None = None

    # @field_validator("cpf")
    # def validate_cpf(cls, v: str | None):
    #     if v is None:
    #         return v
    #     if len(v) != 11:
    #         raise ValueError("CPF must have 11 digits")
    #     return v

    # @field_validator("cnpj")
    # def validate_cnpj(cls, v: str | None):
    #     if v is None:
    #         return v
    #     if len(v) != 14:
    #         raise ValueError("CNPJ must have 14 digits")
    #     return v


class Address(BaseModel):
    city: str
    state: str


class Farm(BaseModel):
    id: str = uuid4().hex
    name: str
    address: Address
    area_in_hec: float
    arable_area_in_hec: float
    vegetation_area_in_hec: float
    cultures: List[str] = []

    # @field_validator("area_in_hec")
    # def validate_area(cls, v: float):
    #     if v <= 0:
    #         raise ValueError("Area must be greater than 0")
    #     if cls.arable_area_in_hec + cls.vegetation_area_in_hec > v:
    #         raise ValueError(
    #             "Arable area and vegetation area must be less than total area"
    #         )
    #     return v
