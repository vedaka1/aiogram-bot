import traceback

from deep_translator import GoogleTranslator


def get_translate(text: str, lang: str) -> str:
    """Translates text into the target language"""
    google = GoogleTranslator(source="auto", target=lang)
    try:
        result = google.translate(text)
        return result
    except Exception:
        print(traceback.format_exc())
        return "There is a error"
