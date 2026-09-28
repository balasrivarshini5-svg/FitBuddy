from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes_new import router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="FitBuddy")

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

app.include_router(router)