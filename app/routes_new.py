from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@router.post("/generate")
async def generate(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "name": "Test User",
            "bmi": "Demo",
            "calories": "Demo",
            "tip": "Stay active!",
            "plan": "<h3>FitBuddy Plan</h3><p>Your plan was generated successfully.</p>"
        }
    )