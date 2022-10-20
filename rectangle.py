#Créez un script rectangle.py#
#Le programme attend deux inputs : la largeur puis la hauteur.
#Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
#   des “|” pour dessiner les côtés droite et gauche
#   des “-” pour dessiner le haut et le bas
#   des espaces pour remplir le rectangle
#
#Exemple pour un input de 10 en largeur et 3 en hauteur
#|--------|
#|        |
#|--------|


largeur = int(input("Nombre de largeur du rectangle : "))
hauteur = int(input("Nombre de haut du rectangle : "))

for i in range(hauteur):
    rectangle="|"
    for j in range(largeur-1):
        if i==0 or i==(hauteur-1):
            rectangle+="-"
        else:
            rectangle+=" " 
    rectangle+="|"
    print(rectangle)





