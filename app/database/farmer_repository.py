from typing import List
from uuid import uuid4

from app.errors import FarmerNotFoundError
from app.models import Farmer

farmers = [
    Farmer(id=uuid4().hex, cpf="12345678909", name="Pedro"),
    Farmer(id=uuid4().hex, cpf="12345678909", name="João"),
    Farmer(id=uuid4().hex, cpf="12345678909", name="Maria"),
]


def create_farmer(farmer: Farmer) -> Farmer:
    farmers.append(farmer)
    return farmer


def get_farmers() -> List[Farmer]:
    return farmers


def get_farmer_by_id(id: str) -> Farmer:
    farmer = list(filter(lambda farmer: farmer.id == id, farmers))
    if not farmer:
        raise FarmerNotFoundError(id)
    return farmer[0]


def update_farmer(id: str, farmer: Farmer) -> Farmer:
    farmer_to_update = get_farmer_by_id(id)
    farmer_to_update.name = farmer.name
    farmer_to_update.cpf = farmer.cpf
    return farmer_to_update


def delete_farmer(id: str) -> None:
    farmer_to_delete = get_farmer_by_id(id)
    farmers.remove(farmer_to_delete)
