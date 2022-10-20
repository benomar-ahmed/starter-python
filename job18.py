#Créer un script job18.py
#Le programme devra contenir une fonction qui prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
#       - Remplir une liste myList contenant tous ces paramètres.
#       - Trier par ordre croissant la liste à l’aide de la fonction sort
#       - Afficher la liste dans un terminal


def myFunction(*args):
    myList=[]
    for i in args:
        myList+=[i]
    return sorted(myList)


print(myFunction(9,1,2,5,6,4,7,3,8))