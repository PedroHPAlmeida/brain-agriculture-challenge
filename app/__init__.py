from fastapi import FastAPI

from .controllers import farmer_router

app = FastAPI()
app.include_router(farmer_router)
