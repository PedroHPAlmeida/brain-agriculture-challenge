from app.controllers.requests import FarmerRequest, FarmRequest
from app.models import Farm, Farmer


def to_farmer(farmer_req: FarmerRequest) -> Farmer:
    return Farmer(name=farmer_req.name, cpf=farmer_req.cpf, cnpj=farmer_req.cnpj)


def to_farm(farm_req: FarmRequest) -> Farm:
    return Farm(
        name=farm_req.name,
        address=farm_req.address,
        area_in_hec=farm_req.area_in_hec,
        arable_area_in_hec=farm_req.arable_area_in_hec,
        vegetation_area_in_hec=farm_req.vegetation_area_in_hec,
        cultures=farm_req.cultures,
    )
