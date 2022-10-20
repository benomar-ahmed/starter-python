#Créez un script job05.py
#L’utilisateur devra entrer deux valeurs en input.
#affichez uniquement les nombres se trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et aller jusqu’à l’input 2.
#Si les deux sont égaux, le programme devra écrire “Valeurs égales”.



val1 = int(input("Valeur 1 : "))
val2 = int(input("Valeur 2 : "))

for i in range(val1+1,val2,++1):
    print(i)
for i in range(val1-1,val2,-1):
    print(i)
if val1==val2:
    print("Valeurs égales")
