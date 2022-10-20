#Créez un script job11.py
#Parcourir le contenu du fichier “domains.xml” et qui compte le nombre de noms de domaine.
#Comptez le nombre de noms de domaine.

fichier = open("domains.xml", "r")
word = fichier.read()
print(len(word.split('"domain">')))




