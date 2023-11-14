from googletrans import Translator, constants

def traducirEn2Es(text):
    translator = Translator()
    translation = translator.translate(text, src="en", dest="es")
    return translation.text