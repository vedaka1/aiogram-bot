import traceback

from deep_translator import GoogleTranslator

from infrastructure.ioc import init_logger


def get_translate(text: str, lang: str) -> str:
    """Translates text into the target language"""
    logger = init_logger()
    google = GoogleTranslator(source="auto", target=lang)
    try:
        result = google.translate(text)
        return result
    except Exception:
        logger.error("Translation error: %s", (traceback.format_exc()))
        return "There is a error"
