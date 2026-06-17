from src.gemini_setup import model

def generate_study_plan(text):

    prompt = f"""
    Create a 7-day study plan.

    Study Time:
    2 hours/day

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text