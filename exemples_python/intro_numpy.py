
# coding: utf-8

# # Brève introduction à Numpy
# `numpy` est un module particulier, qui implémente de nouveaux types de variables: les tableaux multidimensionnels de nomnbres. Ce module implémente également des fonctions compilées qui sont très efficaces lorsqu'elles sont effectuée globalement sur ces tableaux.

# ## Premier exemple de vectorisation 
# On importe le module `numpy` et on le nomme `np` pour simplifier l'écriture ensuite.

# In[1]:


import numpy as np


# On peut utiliser le module `time` pour mesurer le temps d'exécution du code. Il existe une meilleure solution qui s'appelle `timit`, mais qui d'utilisation plus technique.

# In[2]:


import time


# Supposons par exemple que l'on veut calculer la somme de $k=0$ à $p$ des sommes $0 \le i < 10^k$ de $10^{-k}$, qui est en théorie égale à $p+1$.

# In[4]:


p = 7
t1 = time.clock()
S = 0.0
for k in range(p+1):
    for i in range(10**k):
        S = S + 10.0**(-k)
t2 = time.clock()
print("Somme : {0:13.6e} -- erreur : {1:13.6e} -- durée : {2:13.6e}".
      format(S,p+1-S,t2-t1))


# Ci-dessus, l'affichage a été mis en forme avec la fonction `format()` de python (python 3 seulement).

# À la place, on peut, par exemple, créer un tableau pour chacune des étapes (boucle $i$ ci dessous), et observer que le calcul est beaucoup plus rapide.

# In[5]:


t1 = time.clock()
S = 0.0
for k in range(p+1):
    N = np.ones(10**k) * 10**(-k)
    S = S + np.sum(N)
t2 = time.clock()
print("Somme : {0:13.6e} -- erreur : {1:13.6e} -- durée : {2:13.6e}".
      format(S,p+1-S,t2-t1))


# ## Exemples de déclaration de tableaux
# Et voici quelques exemples de déclaration de tableau.

# In[6]:


a = np.array([1,3,2,0,1,-4])
print("a = \n{} est de type {}".format(a,type(a)))

b = np.array([[4.,2.],[1.,3.]])
print("b = \n{} est de type {}".format(b,type(b)))


# Les fonctions ci-dessous permettent d'initialiser des tableaux à des valeurs courantes: $0$, $1$, une suite de nombre. Par ailleurs, ils servent à réserver a priori la mémoire pour un tableau lorsque l'on connait sa taille à l'avance.

# In[16]:


print(np.zeros((2,10))) # crée un tableau de float
print(np.ones((3,4)))   # idem 
print(np.arange(5))     # crée un tableau d'int
print(np.arange(5, dtype=float)) # pour forcer un float


# D'autres fonctions utiles:
# - `np.linspace` : maillage régulier d'un intervalle 1D
# - `np.eye`, `np.identity` : matrice identité
# - `np.meshgrid`, `np.mgrid` : maillages d'un rectangle 2D
# - ...

# In[12]:


print(np.eye(4,2))
print(np.identity(3))


# ## Indices et méthodes d'interrogation des tableaux
# Les indices commencent à 0, et on peut considérer des parties de tableaux en désignant leurs indices. Il existent de nombreuses possiblités pour cela.

# In[13]:


print("a[0] = {} et b[0] = {}".format(a[0],b[0,0]))
print("a[1:3] = {}".format(a[1:3])) # indices 1 et 2
print("b[1,:] = {}".format(b[1,:])) # toute la ligne 1


# Il existent de nombreuses méthodes sur ces tableaux, en voici quelques unes pour connaître la taille ou le type de données du tableau, entre autres.

# In[9]:


print(a.shape, a.dtype) # Bien noter que a est déclaré avec des entiers (sans le .)
print(b.shape, b.dtype) # alors que b est déclaré avec des float (avec le . décimal).
print("Is the number 2 in the array a ? {}".format(2 in a))
print("Is the number 2 in the array b ? {}".format(2 in b))


# ## Forme, copies
# Pour changer la forme d'un tableau, sans changer le nombre total d'éléments, on utilise la fonction `reshape()`.

# In[15]:


c = a.reshape((3,2))
print("a vaut {} et a.reshape((2,3)) vaut \n{}".format(a,c))


# **Attention**, l'association `=` ne crée pas toujours un nouveau tableau, mais plutôt un nouvel identifiant sur la même zone mémoire.

# In[16]:


d = c
c[0,0] = 10
# Mais les deux identifiant pointent vers la même zone mémoire
print("c vaut \n{}".format(c))
print("d vaut \n{}".format(d))


# Les deux identifiants pointe vers le même tableau, il s ont donc la même valeur, bien que seul `c[0,0]` est été modifié. Pour créer une copie d'un tableau, il faut utiliser `copy()`.

# In[17]:


d = c.copy()
c[0,0] = 100
print("c vaut \n{}".format(c))
print("d vaut \n{}".format(d))


# ## Opérations
# Les opérations habituelles, $+$, $-$, $*$, $/$ sont distribués sur les éléments des tableaux, de même que les fonctions trigonométriques, puissance, logarithmiques, etc. Pour cela, il faut utiliser les fonction du module `numpy`.

# In[19]:


x = np.array([1.,2.,3.])
y = np.array([1.,0.,2.])
M = np.array([[4.,2.,0.],
              [2.,4.,2.],
              [0.,2.,4.]])
print("x = \n{}\ny = \n{}\nM = \n{}".format(x,y,M))
# x+y, x-y, se comportent comme prévu
print(x,y,x+y,x-y)
# x*y et x/y distribuent les opérations sur les tableaux
print(x,y,x*y,y/x,x/y) # Notons que la division par 0 n'est qu'un avertissement. Le calcul peut continuer


# On peut avoir des surprses parce que numpy repète un tableau pour le mettre à la bonne taille chaque fois que c'est possible. Par exemple `M+x` semble impossible, mais en fait `+` va répeter `x` en face de chaque ligne de `M`.

# In[20]:


print(M+x)


# Les fonctions trigonométriques, la fonction racine carrée, etc sont distribuées.

# In[22]:


print("sin(x) = {} et sqrt(x) = {}".format(np.sin(x), np.sqrt(x)))


# Les nombres $\pi$ et $\text{e}$ sont donc connus du module `numpy`.

# In[24]:


print("pi = {} et e = {}".format(np.pi, np.e))


# Il existe aussi des fonctions globales sur les tableaux, et des méthodes pour faire des comparaisons, trouver des indices, etc.

# In[27]:


print("La somme des coefficients de M est {} et leur produit est {}".
      format(np.sum(M), np.prod(M)))
print("Rappelons que x = {} et y = {}".format(x,y))
print("x = y ? {} \nx >= y ? {}".format(x==y,x>=y))
print("all(x = y) ? {} \nall(x >= y) ? {}".format(np.all(x==y),np.all(x>=y)))
print("any(x = y) ? {} \nany(x >= y) ? {}".format(np.any(x==y),np.any(x>=y)))


# ## Algèbre linéaire
# Le produit matriciel, au sens mathématique, est réalisé par la fonction `dot()`., Il existe aussi
# - `np.outer` : produit extérieur
# - `np.inner` : produit scalaire
# - `np.cross` : produit vectoriel
# Et dans le sous-module `np.linalg`, on trouve les méthodes
# - `np.linalg.solve` : résolution d'un système linéaire
# - `np.linalg.eig` : valeurs propres et vecteurs propres

# In[20]:


y = np.dot(M,x)
print("M*x = {}".format(y))
M_carre = np.dot(M,M)
print("M^2 = \n{}".format(M_carre))

z = np.linalg.solve(M,y)
print("Solution de Mx=y : {}".format(z))
print("Vecteur erreur : {}, \net sa norme : {:}".format(x-z, np.linalg.norm(x-z)))
[D,P] = np.linalg.eig(M)
print("Les valeurs propres de M : {}".format(D))


# ## Aide
# On peut voir ce qui est disponible dans ce sous-module avec l'aide.

# In[32]:


help(np.linalg)


# L'aide complète de `numpy` est disponible aussi. Elle est plus longue, et ne rentre pas dans ce document. Par contre, on peut voir la documentation de la méthode de résolution des systèmes linéaires.

# In[34]:


help(np.linalg.solve)

