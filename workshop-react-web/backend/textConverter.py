import gptApi
import translator
import dicta

from checktext import allChecks

def simplify(text: str, level: int):
    #text2=allChecks(text)
    print(text)
    english_text = translator.text_translator(text, 'he', 'en')
    print(english_text)
    print("------------")

    if(level==1):
        simplified_text = gptApi.gpt_wrapper.simplify_5_years_old(english_text)
    elif(level==2):
        simplified_text = gptApi.gpt_wrapper.simplify_10_years_old(english_text)
    elif(level==3):
        simplified_text = gptApi.gpt_wrapper.cognitive_problems(english_text)
    else:
        simplified_text = gptApi.gpt_wrapper.simplify_10_years_old(english_text)

    print(simplified_text)
    print("--------")
    hebrew_text = translator.text_translator(simplified_text, 'en', 'he')
    return hebrew_text #dicta.dictate(hebrew_text)


print(simplify(""" אקלים הוא אוסף של מאפיינים מטאורולוגיים, ובעיקר טמפרטורות ומשקעים, ועננות הקובעים את סיווגו של אזור גאוגרפי מסוים מבחינת מזג האוויר השורר בו לאורך השנה.""",3    ))