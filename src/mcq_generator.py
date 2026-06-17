from src.gemini_setup import model

def generate_mcqs(text):

    prompt = f"""
    Generate 20 MCQs.

    Format:

    Question

    A)
    B)
    C)
    D)

    Correct Answer

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text