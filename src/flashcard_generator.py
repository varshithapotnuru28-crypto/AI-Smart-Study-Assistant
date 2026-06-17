from src.gemini_setup import model

def generate_flashcards(text):

    prompt = f"""
    Create flashcards.

    Format:

    Question:
    Answer:

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text