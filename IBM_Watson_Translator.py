'''
This program is a translator that uses IBM Watson's Language Translator Service.
You need an IBM Bluemix account to access the service.
'''
import requests
 
def cls():
    print("\n" * 5)
 
def translate_text(text,source,target):
    username = '614105fe-6379-4bcd-8253-c3a76ba92c1f'
    password = 'KZ7msi8EqnmD'
    watsonUrl = 'https://gateway.watsonplatform.net/language-translation/api/v2/translate?source=' + source + '&target=' + target + '&text=' + text
    try:
        r = requests.get(watsonUrl,auth=(username,password))
        #print(r)
        return r.text
    except:
        return False
 
def welcome():
    message = "Welcome to the IBM Watson Translator\n"
    print(message + "-" * len(message) + "\n")
    print("Have fun!\n")
 
def main():
    cls()
    welcome()
 
    data = input("Enter some text to be translated:\n")
 
    print()
    print("What language should I translate it to?")
    print("1) Spanish")
    print("2) Arabic")
    print("3) French")
    print("4) Portuguese")
    print()
    target = input("Select a language from the list above: ")
 
    if target == "1":
        target = 'es'
    elif target == "2":
        target = 'ar'
    elif target == "3":
        target = 'fr'
    elif target == "4":
        target = 'pt'
 
    results = translate_text(data,'en',target)
    print()
    print("Here is the text translated for you:")
    print(results)
 
main()
