# -*- coding: utf-8 -*-

# Le type 'bool' est celui qui apparait lorsque l'on calcule des
# conditions, par exemple
x,y = 2.0,3
test = (x==y) # qui vaut True ou False
print(test, type(test))

x,y = 2.0,2
test = (x==y) # Il y a une conversion automatique avant le test, sinon
              # la comparaison ne peut pas avoir lieu.
print(test, type(test))

# etc, there are several important data structures in python,
# e.g. dictionnaries, lists, tuples, etc.

# Je n'introduit ici que les listes
a = [1,2,4,8,16] # c'est une suite (finie)
print(a, type(a))

# On peut y mettre de variable de types différents
a = [1,0,3.14,"moi-même"]

# Construire une liste de manière dynamique
a.append(0.5)
print(a)

# Interroger la liste. Les items de la liste sont numérotés à partir de 0.
print("len(a) =",len(a), "a[0] =",a[0], "a[3] =",a[3])

# On peut mettre une liste dans une liste
b = [a, "et moi"]
print("b = [a, 'et moi'] =", b)

# Faire une liste vide
b = []
print("b =",b)

# Autres types de données: tuple, set, dictionary

# Le range est aussi une classe, qui est en réalité une manière de créer
# des itérations dans une suite de nombres.
print(range(5)) # Suite partant de 0 (par défaut) et <5, donc 0, 1, 2, 3, 4
print(range(1,5)) # même chose à partir de 1, donc 1, 2, 3, 4
print(range(1,5,2)) # même chose en itérant de 2 en 2, donc 1, 3

# On peut convertir un range en une list pour mieux comprendre de quoi
# il s'agit:
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,5,2)))
