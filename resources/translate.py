from deep_translator import GoogleTranslator
import traceback

google = GoogleTranslator(source='auto', target='ru')   
def get_translate(text):
    try:
        result = google.translate(text)
        return result
    except:
        print(traceback.format_exc())
