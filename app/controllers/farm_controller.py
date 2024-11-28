from typing import List

from fastapi import APIRouter

from app.database import farmer_repository as repository
from app.models import Farmer

router = APIRouter(prefix="/api/v1/farms")


@router.get("/", status_code=200)
def get_farms() -> List[Farmer]:
    return [f.model_dump() for f in repository.get_farmers()]


@router.get("/{farmer_id}")
def get_farm_by_id(farmer_id: int) -> Farmer:
    return repository.get_farmer_by_id(farmer_id), 200


@router.post("/")
def create_farm() -> Farmer:
    return {"message": "Hello World"}


@router.put("/{farmer_id}")
def update_farm(farmer_id: int):
    return {"message": "Hello World"}


@router.delete("/{farmer_id}")
def delete_farm(farmer_id: int):
    return repository.delete_farmer(farmer_id), 200
