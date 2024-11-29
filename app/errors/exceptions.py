from fastapi import HTTPException


class FarmerNotFoundError(HTTPException):
    def __init__(self, id: str) -> None:
        super().__init__(404, f"Farmer with id '{id}' not found", None)


class FarmNotFoundError(HTTPException):
    def __init__(self, id: str) -> None:
        super().__init__(404, f"Farm with id '{id}' not found", None)


class InvalidAreaError(HTTPException):
    def __init__(self, area: float) -> None:
        super().__init__(400, f"Area '{area}' is invalid", None)
