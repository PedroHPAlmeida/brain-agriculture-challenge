from typing import List
from uuid import uuid4

from app.errors import FarmNotFoundError
from app.models import Address, Farm

farms = [
    Farm(
        id=uuid4().hex,
        name="Farm 1",
        address=Address(city="São Paulo", state="SP"),
        area_in_hec=100,
        arable_area_in_hec=50,
        vegetation_area_in_hec=50,
        cultures=["Corn", "Soybean"],
    ),
    Farm(
        id=uuid4().hex,
        name="Farm 2",
        address=Address(city="Rio de Janeiro", state="RJ"),
        area_in_hec=200,
        arable_area_in_hec=100,
        vegetation_area_in_hec=100,
        cultures=["Corn", "Soybean", "Wheat"],
    ),
    Farm(
        id=uuid4().hex,
        name="Farm 3",
        address=Address(city="Belo Horizonte", state="MG"),
        area_in_hec=300,
        arable_area_in_hec=150,
        vegetation_area_in_hec=150,
        cultures=["Corn", "Soybean", "Wheat", "Cotton"],
    ),
]


def get_farms() -> List[Farm]:
    return farms


def get_farm_by_id(farm_id: str) -> Farm:
    farm = list(filter(lambda f: f.id == farm_id, farms))
    if not farm:
        raise FarmNotFoundError(farm_id)
    return farm[0]


def create_farm(farm: Farm) -> Farm:
    farms.append(farm)
    return farm


def update_farm(farm_id: str, farm: Farm) -> Farm:
    farm = get_farm_by_id(farm_id)
    return farm


def delete_farm(farm_id: str) -> None:
    farm = get_farm_by_id(farm_id)
    farms.remove(farm)
