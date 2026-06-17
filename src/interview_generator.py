from src.gemini_setup import model

def generate_interview_questions(text):

    prompt = f"""
    Generate:

    10 Beginner Questions

    10 Intermediate Questions

    10 Advanced Questions

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text