from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    goal: str # Weight Loss, Muscle Gain, Fitness
    diet_type: str # Veg, Non-Veg, Vegan
    workout_days: int = 5