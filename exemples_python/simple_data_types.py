# -*- coding: utf-8 -*-

# La ligne ci dessus est un commentaires spécial, qui indique que les caractères
# de ce fichier sont encodés sur le disque dur avec le protocole utf8. Celui-ci
# est relativement universel et permet d'encoder tous les caractères du français
# (y compris, accents, cédilles, ets) et de nombreuses autres langues (grec,
# cyrilique par exemple).

# Une variable python est repérée par un identifiant, qui est composé de
# caractères non accentués, sans espaces, et quelques autres règles. Par
# exemple, on peut affecter la valeur 1.0 à la variable d'identifiant a. Plus
# simplement, on parle de la variable a.
a = 1.0
# Cela signifie que le code binaire pour représenter 1.0 est enregistré quelque
# part en mémoire et que a fait référence à cet emplacement.

# Le type de variable est le type d'objet que l'on stocke en mémoire. Ilest donc
# lié avec une représentation en machine de cet objet. En python, il existe les
# types suivants:

# Nombres réels à virgule flottante (voir norme IEEE-754) -- float
x = 0.1
# La fonction print affiche la valeur de la variable. La fonction type renvoie
# le type d'une variable.
print(x, type(x))

# Entiers -- integer
n = 1
print(n, type(n))

# Chaine de caractère
s = "Bonjour, je suis une chaîne de caractère, avec des caractères typiquement français, qui n'ont pas de code Ascii"
print(s, type(s))
