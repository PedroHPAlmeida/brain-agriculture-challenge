from fastapi import FastAPI

from .controllers import farm_router, farmer_router

app = FastAPI(title="Brain Agriculture", summary="Brain Agriculture Management System", version="1.0.0")
app.include_router(farmer_router)
app.include_router(farm_router)
