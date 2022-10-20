#Créez un script job06.py
#Écrire un programme qui parcourt les nombres entiers de 1 à 100.
#Pour les multiples de trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz"
#Pourles nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".


for i in range(0,101,++1):
    if (i%3==0) and (i%5==0):
        i="FizzBuzz"
        print(i)
        continue
    elif i%3==0:
        i="Fizz"
        print(i)
        continue
    elif i%5==0:
        i="Buzz"
        print(i)
        continue
    print(i)



