#Créez un script job16.py
#Le programme devra contenir une fonction qui prend en paramètres un nombre de paramètres indéfini.
#La fonction écrira tous les paramètres dans le terminal.

def myFunction(*args):
    print(args)


myFunction("tata","titi","tata")