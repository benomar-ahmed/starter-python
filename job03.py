#Créez un script job03.py#
#Afficher la phrase “Bonjour, quel âge as tu ? ”
#L’utilisateur devra ensuite entrer son âge.
#Déclarez une variable “âge”, qui prendra la valeur saisie par l’utilisateur.
#Affichez “Tu es mineur” si l’âge est inférieur à 18 et “Tu es majeur” si l’âge est supérieur ou égal à 18.


age = int(input("Quel âge as-tu ? "))
if age < 18:
    print("Tu es mineur ")
else:
    print("Tu es majeur")
