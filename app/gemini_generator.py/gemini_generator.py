import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_plan_with_gemini(user_data, bmi, calories):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    You are FitBuddy AI Trainer. Create a detailed plan.
    User: {user_data.name}, Age {user_data.age}, Weight {user_data.weight}kg, Height {user_data.height}cm
    BMI: {bmi}, Target Calories: {calories}, Goal: {user_data.goal}, Diet: {user_data.diet_type}, Workout Days: {user_data.workout_days}
    
    Give response in 3 sections:
    1. DIET PLAN (Morning, Afternoon, Night with calories)
    2. WORKOUT PLAN (Day wise exercises)
    3. TIPS
    Use HTML formatting with <h3>, <ul>, <li>, <b>.
    """
    response = model.generate_content(prompt)
    return response.text