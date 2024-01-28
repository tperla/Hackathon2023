import googletrans

def text_translator(text, origin_lang, target_lang):
    translator = googletrans.Translator()
    translation = translator.translate(text, src=origin_lang, dest=target_lang)
    return translation.text.replace('\\n', '\n')