from src.gemini_setup import model

def generate_notes(text):

    prompt = f"""
    Create detailed study notes.

    Use:
    - Headings
    - Subheadings
    - Bullet points

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text