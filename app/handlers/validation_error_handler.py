import json

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError


def validation_error_handler(app: FastAPI):
    @app.exception_handler(ValidationError)
    async def handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=400,
            content={"message": "Validation error", "detail": json.loads(exc.json())},
        )

    return handler
