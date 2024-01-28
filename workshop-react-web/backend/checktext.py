from trancheck import rashei_Tevot
from operator import length_hint
from num2words import num2words
import inflect

     


def number_to_words(number):
    ones = ['אפס', 'אחד', 'שניים', 'שלוש', 'ארבע','חמש', 'שש', 'שבע', 'שמונה', 'תשע']
    once2 = ['אפס', 'ואחד', 'ושניים', 'ושלוש', 'וארבע', 'וחמש', 'ושש', 'ושבע', 'ושמונה', 'ותשע']
    tens = ['עשר', 'עשרים', 'שלושים', 'ארבעים', 'חמישים', 'שישים', 'שבעים', 'שמונים', 'תשעים']
    hundreds = ['מאה', 'מאתיים', 'שלוש מאות', 'ארבע מאות', 'חמש מאות', 'שש מאות', 'שבע מאות', 'שמונה מאות', 'תשע מאות']
    powers_of_thousand = ['', 'אלף', 'מיליון', 'מיליארד', 'טריליון', 'קוודריליון', 'קוינטיליון', 'סקסטיליון', 'ספטיליון', 'אוקטיליון', 'נוניליון', 'דציליון', 'אן ויגינטיליון']
   
    if number == 10:
        return 'עשר'
    if number >= 0 and number < 10:
        return ones[number]   
    words = []
    power = 0
   
    while number > 0:
        current_word = ''
        current_number = number % 1000
        number = number // 1000
       


        if current_number >= 100:
            current_word += hundreds[current_number // 100 - 1] + ' '
            current_number %= 100
       
        if current_number >= 20:
            current_word += tens[current_number // 10 - 1] + ' '
            current_number %= 10


        if current_number >10 and current_number <20:
             current_word += ones[current_number % 10] +' עשרה'

       
       
        if current_number > 1 and current_number<10:
               if current_number == 2 and power >= 2:
                  current_word +='שתי '
               else:
                current_word += once2[current_number] + ' '

        if current_number == 1:
            if power == 2:
               current_word +=" "
            else:
              current_word += once2[current_number] + ' '
       
        if power > 0 and current_word:
            current_word += powers_of_thousand[power] + ' '
       
        words.insert(0, current_word)
        power += 1

        if power > 0 and current_word:
            if power == 1:
                current_word = powers_of_thousand
   
    return ''.join(words)






def allChecks(message : str):
    list=message.split(" ")
    for x in range(len(list)):
        word = list[x]
        #בדיקת מספרים
        # if isinstance(word, int):
        #     list[word.index()] = number_to_words(int(word))
        try:
            num = int(word)
            list[x] = number_to_words(num)
        except:
            pass
        #בדיקת ראשי תיבות
       # if "\"" in word and not (word.startswith('\"') or word.endswith('\"')):
          ##   parts = word.split('\"')
           #  if len(parts) == 2:
             #   abc='abcdefghijklmnopqrstuvwxyz'
             #   if parts[0][-1].lower() in abc and parts[1][0].lower() in abc :
              #      list[x] = rashei_Tevot(int(word))
        #בדיקת מושגים שיש להשאיר כמו שהם
        #if word[0]=="\'" or word[0]=="\"":
            #if word[-1]=="\"" or word[-1]=="\'":
    return ' '.join(list)

        








