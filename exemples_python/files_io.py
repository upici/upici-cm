# -*- coding: utf-8 -*-

# Pour ouvrir, écrire et lire dans un fichier, il existe de nombreuses
# méthodes. De manière générale:
fid = open("test.txt","w", encoding="utf-8")
# "w" pour une ouverture en écriture, "r" pour lire, il existe d'autres
# possibilités. Pour un fichier texte, on peu spécifier l'encodage des
# caractères.

# Écriture en elle-même
fid.write("mon premier fichier ")
fid.write("et ceci continue sur la même ligne \n")
fid.write("et maintenant sur une nouvelle ligne \n")

# Pour afficher des nombres, il faut les formatter comme un chaine de
# caractère, par exemple comme ci-dessous. Voir le doc pour plus
# d'exemples et une description plus complète.
fid.write("{0} \n".format(list(range(10))))

# On peut aussi faire une boucle
for i in range(10):
    fid.write("{0} ".format(i))

# Et la fermeture
fid.close()


# Pour ne pas avoir à ouvrir puis fermer le fichier, on peut utiliser la
# syntaxe suivante
with open("test.txt", "w", encoding = "utf-8") as fid:
    fid.write("mon premier fichier ")
    fid.write("et ceci continue sur la même ligne \n")
    fid.write("et maintenant sur une nouvelle ligne \n")
    fid.write("{0} \n".format(list(range(10))))

# Et du coup, le fid.close() est fait automatiquement.

