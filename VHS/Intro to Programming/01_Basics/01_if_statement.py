print("Available Languages:")
print("[1] DE")
print("[2] EN")
print("[3] FR")

# Ask user language
user_lang = int(input("Select a number for your language: "))

if user_lang == 1:
    print('Willkommen bei Telekom')
elif user_lang == 2:
    print('Welcome at Telekom')
elif user_lang == 3:
    print('Bienvenue a Telecom')
else:
    print('Sorry, we do not offer this language. We will continue in English')

######################################
# Nestet if (sub if)

age = 25
items = 0

if age >= 18:
    if items > 0:
        print('Zur Kasse bitte!')
    else:
        print('Du musst Produkte auswählen')
else:
    print('Du bist noch zu jung')
