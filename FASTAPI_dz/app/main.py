from fastapi import FastAPI
from app.routers.filmovi import router as filmovi_router

app = FastAPI()
app.include_router(filmovi_router)
