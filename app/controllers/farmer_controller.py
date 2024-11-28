from typing import List

from fastapi import APIRouter

from app.database import farmer_repository as repository
from app.models import Farmer
from app.utils import utils

from .requests import FarmerRequest

router = APIRouter(prefix="/api/v1/farmers", tags=["Farmers"])


@router.get("/", status_code=200)
def get_farms() -> List[Farmer]:
    return repository.get_farmers()


@router.post("/", status_code=201)
def create_farmer(farmer: FarmerRequest) -> Farmer:
    return repository.create_farmer(utils.to_farmer(farmer))


@router.get("/{farmer_id}", status_code=200)
def get_farm_by_id(farmer_id: str) -> Farmer:
    return repository.get_farmer_by_id(farmer_id)


@router.put("/{farmer_id}", status_code=200)
def update_farmer(farmer_id: str, farmer: FarmerRequest) -> Farmer:
    return repository.update_farmer(farmer_id, utils.to_farmer(farmer))


@router.delete("/{farmer_id}", status_code=204)
def delete_farm(farmer_id: str) -> None:
    repository.delete_farmer(farmer_id)
