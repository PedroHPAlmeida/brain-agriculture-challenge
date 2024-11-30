from fastapi import FastAPI

from .controllers import farm_router, farmer_router
from .handlers import validation_error_handler

app = FastAPI(title="Brain Agriculture", summary="Brain Agriculture Management System", version="1.0.0")

validation_error_handler(app)

app.include_router(farmer_router)
app.include_router(farm_router)
