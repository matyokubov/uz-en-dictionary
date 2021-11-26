from uz_en_dictionary import Translator
from uz_en_dictionary import Dictionary

class App:
    def search(word, d, l):
        getResult = d.search(word)
        if(not getResult): 
            print(f"\nResult [{word}]: ----\n")
        else:
            print(f"\nResult [{word}]: {list(getResult.keys())}\n")
        App.selectWord(l)
    
    def transText(word, t, l):
        getResult = t.translate(word)
        if(not getResult): 
            print(f"\nResult [{word}]: ----\n")
        else:
            print(f"\nResult [{word}]: {getResult}\n")
        App.selectWord(l)

    def selectWord(lang):
        if(lang == "en" or lang == "uz"):
            word = input(f"Search [{lang}]: ")
            d = Dictionary(lang)
            App.search(word.replace("`", "'"), d, lang)
        elif(lang == ['uz', 'en'] or lang == ['en', 'uz']):
            word = input(f"Enter the word [{lang[0]}]: ")
            t = Translator(lang[0], lang[1])
            App.transText(word.replace("`", "'"), t, lang)

    def selectLang():
        print('''Enter Language:
1. English -> Uzbek
2. Uzbek -> English
3. Search English word
4. Search Uzbek word
''')
        try:
            lang = int(input("Language number: "))
            if(lang > 4 or lang < 1):
                print(f"No command {lang}")
                App.selectLang()
            select = {'1': ['en', 'uz'], '2': ['uz', 'en'], '3': 'en', '4': 'uz'}
            App.selectWord(select[str(lang)])
        except ValueError:
            print(f"Error command")
            App.selectLang()
        
    def main():
        print('''
===== English-Uzbek Dictionary & Translator =====
Created: 20.11.2021
Author: Matyoqubov Firdavs
''')
        App.selectLang()

App.main()
