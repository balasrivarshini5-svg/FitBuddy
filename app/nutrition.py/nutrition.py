def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def calculate_calories(weight, height, age, goal):
    # Mifflin-St Jeor (male avg)
    bmr = 10*weight + 6.25*height - 5*age + 5
    if goal == "Weight Loss":
        return int(bmr * 1.2 - 300)
    elif goal == "Muscle Gain":
        return int(bmr * 1.4 + 300)
    else:
        return int(bmr * 1.3)