# -*- coding: utf-8 -*-

import numpy as np

# Et on va faire des graphes en utilisant matplotlib
import matplotlib.pyplot as plt

# On commence par construire les tableaux de nombres pour les abcisses
# et ordonnées. On échantillone pour prendre 101 valeurs de x allant de
# -pi à pi.
x = np.linspace(-np.pi, np.pi, 101)
# et on prend y = cos(x) et z = sin(x)
y,z = np.cos(x), np.sin(x)

plt.plot(x,y, color='red',   linestyle='-', linewidth=3., label='cos')
plt.plot(x,z, color='black', linestyle=':', linewidth=3., label='sin')

plt.legend() # pour afficher la légende, il y a des options possible (frameon, loc...)
plt.show()

# Pour tracer une surface
from mpl_toolkits.mplot3d import Axes3D

# On commence par échantilloner la surface
x = np.linspace(-4, 4, 21)
y = np.linspace(-4, 4, 21)
# Ceci construit des tableaux à 2 dimensions contenant les x et les y
x, y = np.meshgrid(x, y)
# On calcule les valeurs de la fonction dont on veut tracer le graphe
r = np.sqrt(x**2 + y**2)
z = r**2#np.sin(r)

# On ouvre une figure en 3D
fig = plt.figure()
ax = Axes3D(fig)

# On trace la surface
ax.plot_surface(x, y, z, cmap='hot')

plt.show()

