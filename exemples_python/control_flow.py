# -*- coding: utf-8 -*-

# Bien sur python permet de faire des boucles et d'exécuter des portions
# de code sous condition.

# Exécution conditionnelle
a,b = 1,1
if a==b:
    # Ce qu'il faut faire si a=b
    print("nous sommes dans le cas où a=b")
else:
    # et sinon ?
    print("que faire si a~=b ?")

# cas plus complexe: la fonction x --> y = max(0,min(x,1))
x = 1.0/3.0
if x<0.:
    y = 0.
elif x<1.:
    y = x
else:
    y = 1.
print("x =",x,"y =",y)

# L'indentation sert à délimité les portions de code qui sont exécuter
# sous condition.

# Boucle. Il existe de très nombreux type de boucles en python.

# Boucle sur un itérateur range
for i in range(5):
    print("i =",i," i^2 =",i**2)

# Boucle sur une liste
i_s = [1,2,3,6,8,9]
for i in i_s:
    print("i =",i," i^2 =",i**2)

# Il existe aussi une boucle "tant que", avec l'instruction while
n = 0
S = 0
while n<10:
    n = n+1
    S = S+n
print("Somme des",n,"premiers entiers =",S)

