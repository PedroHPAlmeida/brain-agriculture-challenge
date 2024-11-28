from fastapi import FastAPI

from .controllers import farm_router, farmer_router

app = FastAPI()
app.include_router(farmer_router)
app.include_router(farm_router)
