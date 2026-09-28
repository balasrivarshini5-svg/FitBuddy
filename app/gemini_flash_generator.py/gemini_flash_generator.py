import google.generativeai as genai
def generate_quick_tip(goal):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Give 1 line motivational fitness tip for {goal}")
    return response.text