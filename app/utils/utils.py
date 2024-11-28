from app.controllers.requests import FarmerRequest
from app.models import Farmer


def to_farmer(farmer_req: FarmerRequest) -> Farmer:
    return Farmer(name=farmer_req.name, cpf=farmer_req.cpf, cnpj=farmer_req.cnpj)
