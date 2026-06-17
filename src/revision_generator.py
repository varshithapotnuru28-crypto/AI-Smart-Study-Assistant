from src.gemini_setup import model

def generate_revision_notes(text):

    prompt = f"""
    Create one-day revision notes.

    Include:
    - Key Concepts
    - Definitions
    - Important Points

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text