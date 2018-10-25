# -*- coding: utf-8 -*-

# Enfin, on peut définir une fonction avec le mot clé def.
def f(x):
    y = 2*x**2 - 1 # fonction 2x^2-1
    return y

# On peut maintenant utiliser cette fonction
print("f(0) =",f(0),"f(1) =",f(1),"f(-1) =",f(-1))

# Et par exemple chercher une racine dans (0,1) par dichotomie
a,b=0.0,1.0
c = 0.5*(a+b)
while abs(f(c))>1.e-6:
    print("c =",c,"f(c) =",f(c))
    if f(a)*f(c)<0.0:
        b = c
    else:
        a = c
    c = 0.5*(a+b)
print("résultat: c =",c,"et f(c) =",f(c))

# Et bien sur, on peut mettre cet algorithme dans une fonction
def dichotomie(f,a,b,tolerance,n_max_iterations):
    if (a>=b):
        print("il faut partir avec a<b, alors que a =",a,"et b =",b)
        return
    if f(a)*f(b)>0.0:
        print("il faut que f(a)*f(b)<0.0, alors que f(a)*f(b) = ",f(a)*f(b))
        return
    c = 0.5*(a+b)
    iter = 0
    while abs(f(c))>tolerance and iter<n_max_iterations:
        if f(a)*f(c)<0.0:
            b = c
        else:
            a = c
        c = 0.5*(a+b)
        iter = iter + 1
    return c,iter

# Que l'on utilise de la manière suivante.
[x,n] = dichotomie(f,0.0,1.0,  1.e-10,100)
print("Méthode de dichotomie, c =",x,"après",n,"itérations")

# Important: on peut mettre les fonctions, ainsi que des définitions de
# variables dans un fichier séparé. Ce fichier contient alors un module
# python. Il peut être importé dans un environnement de travail avec la
# fonction import.

# Il exisge de nombreux modules qui étendent python. Par exemple, pour
# obtenir les fonctions mathématiques usuelles, on utilise le module
# math.
import math
print("cos(0.5) =",math.cos(0.5))
print("sqrt(2)/2 =",0.5*math.sqrt(2))
