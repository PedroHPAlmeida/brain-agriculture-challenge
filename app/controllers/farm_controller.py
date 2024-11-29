from typing import List

from fastapi import APIRouter

from app.database import farm_repository as repository
from app.models import Farm
from app.utils import parsers

from .requests import FarmRequest

router = APIRouter(prefix="/api/v1/farms", tags=["Farms"])


@router.get("/", status_code=200)
def get_farms() -> List[Farm]:
    return repository.get_farms()


@router.get("/{farm_id}", status_code=200)
def get_farm_by_id(farm_id: str) -> Farm:
    return repository.get_farm_by_id(farm_id)


@router.post("/", status_code=201)
def create_farm(farm: FarmRequest) -> Farm:
    return repository.create_farm(parsers.to_farm(farm))


@router.put("/{farm_id}", status_code=200)
def update_farm(farm_id: int, farm: FarmRequest) -> Farm:
    return repository.update_farm(farm_id, parsers.to_farm(farm))


@router.delete("/{farm_id}", status_code=204)
def delete_farm(farm_id: str):
    repository.delete_farm(farm_id)
