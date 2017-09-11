#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Paramètres du système linéaire, y'' + by' + a^2y = 0, qui est un oscillateur
# harmonique (cas b=0) amorti (b>0) ou amplifié (b<0).
a = 1.  # fréquence
b = 0.6 # amortissement
A = np.array([[0.,1.],[-a**2,-b]]) # Matrice du système obtenu par réécriture à
                                   # l'ordre 1 de l'équation

# Bornes du plan de phase que l'on va tracer
xmin,xmax, ymin,ymax = -2.,2., -2.,2.

# Pas en x et y utilisé pour tracer les graphes du plan de phase.
hx = (xmax-xmin)/10.
hy = (ymax-ymin)/10.

# Nullclines

# A_11*x + A_12*y = 0
if not A[0,0]==0.:
    y = np.arange(ymin,ymax+hy,hy)
    x = -A[0,1]*y/A[0,0]
else:
    x = np.arange(xmin,xmax+hx,hx)
    y = -A[0,0]*x/A[0,1]

plt.plot(x,y, linewidth=2)

# A_21*x + A_22*y
if not A[1,1]==0.:
    x = np.arange(xmin,xmax+hx,hx)
    y = -A[1,0]*x/A[1,1]
else:
    y = np.arange(ymin,ymax+hy,hy)
    x = -A[1,1]*y/A[1,0]

plt.plot(x,y, linewidth=2)

# Champ de vecteur f(x,y):= A*[x,y]^T
y,x = np.mgrid[ymin:ymax+hy:hy, xmin:xmax+hy:hx]
u = A[0,0]*x + A[0,1]*y # Champ des vitesses suivant x
v = A[1,0]*x + A[1,1]*y # Champ des vitesses suivant y
speed = np.sqrt(u*u + v*v) # Champ de vitesses

plt.streamplot(x,y,u,v, color=speed, linewidth=1)
plt.axis([xmin,xmax,ymin,ymax])

plt.colorbar()
plt.xlabel("y1")
plt.ylabel("y2)")
plt.title("Plan de phase système linéaire")
plt.grid(True)

# ========================================
# Partie 2, question 3: code à insérer ici
# ========================================

plt.savefig("lineaire.png")
#plt.show()

