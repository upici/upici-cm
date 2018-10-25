# -*- coding: utf-8 -*-

# On peut faire des oprations sur des variables, et affecter les
# résultats à de nouvelles variables, ou pas.

# Des opérations sur des réels
x = 0.5
y = x*x
z = 2*x
t = x/y
print('x =',x,'y = x^2 =',y,'z = 2x =',z,'t = x/y =',t)

# Avec des entiers
n = 2
p = 1/2  # Ceci est la division dans R, le résultat est 0.5
q = 1//2 # la division euclidienne, le résultat est 0
r = 1%2  # le reste dans la division euclidienne, soit 1
print("n =",n,"p = 1/2 =",p,"q = 1//2 =",q,"r = 1%2 = ",r)

# On peut aussi convertir automatiquement des types de variables
x = 0.2 # un float
n = 2   # un int
t = x+n # conversion automatique dans le type qui va bien, float
print(type(x),type(n),type(t))

# Attention, pour les opérations entre des types différents, il n'y a
# pas toujours de conversion qui permet de réaliser l'opération
s = "1234"
x = 2*s # c'est "12341234"
y = x+"abc" # c'est "12341234abc"
print("s =",s,"x = 2*s",x,"y = x+'abc' =",y)
y = s+12 # impossible
