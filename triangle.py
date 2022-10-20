#Créez un script triangle.py#
#Afficher dans le terminal un triangle avec des ‘_’, des ‘\’ et des ‘/’
#L’input entré représentera la hauteur.
#Exemple si l’input entré est 5
#    /\
#   /  \
#  /    \
# /      \
#/________\




hauteur = int(input("Veuillez choisir la hauteur de votre triangle : "))


left="/"
right="\\"
base = '__'

for i in range(hauteur):
    print((hauteur-i) *" " + left + ((i*2) * ' ')+ right)
    if i == hauteur -1:
        print(left + base * hauteur + right)
    

    
    