from deep_translator import GoogleTranslator
import traceback

def get_translate(text, lang):
    google = GoogleTranslator(source='auto', target=lang)   
    try:
        result = google.translate(text)
        return result
    except:
        print(traceback.format_exc())
