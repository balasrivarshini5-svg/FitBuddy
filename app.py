from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

client = genai.Client()


class FitnessRequest(BaseModel):
    name: str
    goal: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/generate")
async def generate_plan(data: FitnessRequest):
    prompt = f"""
Create a simple, safe and age-appropriate general fitness plan.

Name: {data.name}
Goal: {data.goal}

Give:
1. Simple daily activities
2. Beginner-friendly exercises
3. Rest and recovery tips
4. General healthy habits

Do not give extreme exercise, dieting, calorie restriction, supplements,
or weight-loss instructions.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return {"plan": response.text}
