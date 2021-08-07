from deep_translator import GoogleTranslator

language = input("Translate from (en=English, fa=Farsi): ")

if language == "en":
    to_translate = input("Enter your text : ")
    translated = GoogleTranslator(source='en', target='fa').translate(to_translate)
    print(translated)      

if language == "fa": 
    to_translate = input("Enter your text : ")
    translated = GoogleTranslator(source='fa', target='en').translate(to_translate)
    print(translated)  
else:
    print("error")
