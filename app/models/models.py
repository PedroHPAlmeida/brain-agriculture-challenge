from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self

from app.errors import InvalidAreaError
from app.services.validations import is_area_smaller_than_areable_and_vegetation


class Farmer(BaseModel):
    id: str = uuid4().hex
    name: str
    cpf: Optional[str] = None
    cnpj: Optional[str] = None

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
    area_in_hec: float = Field(gt=0, description="Total area in hectares")
    arable_area_in_hec: float = Field(gt=0, description="Arable area in hectares")
    vegetation_area_in_hec: float = Field(gt=0, description="Vegetation area in hectares")
    cultures: List[str] = []

    @model_validator(mode="after")
    def validate_area(self) -> Self:
        is_smaller = is_area_smaller_than_areable_and_vegetation(
            self.area_in_hec, self.arable_area_in_hec, self.vegetation_area_in_hec
        )
        if is_smaller:
            raise InvalidAreaError(self.area_in_hec)
        return self
