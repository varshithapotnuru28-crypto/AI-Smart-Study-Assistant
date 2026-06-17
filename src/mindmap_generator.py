from src.gemini_setup import model

def generate_mindmap(text):

    prompt = f"""
    Create a text-based mind map.

    Example:

    Database
    |
    +-- SQL
    |
    +-- NoSQL

    Content:

    {text[:5000]}
    """

    response = model.generate_content(prompt)

    return response.text