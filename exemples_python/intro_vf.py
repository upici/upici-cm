# coding: utf-8

import numpy as np              # Tableaux efficaces
import scipy.sparse as sp       # Algèbre linéaire creuse
import matplotlib.pyplot as plt # Pour les graphiques

# On cherche à résoudre l'équation
# ```d_t u + d_x[f(u)] = 0```
# pour t>0 et x dans R, avec
#  - f une fonction C^1 convexe de R dans R
#  - u(.,0) = u_0 une donnée initiale à support compact, dans un intervalle [a,b]

# Le schéma volume fini s'écrit alors
# ```u_i^{n+1} = u_i^n - dt/dx * [ F(u_i^n,u_{i+1}^n) - F(u_{i-1}^n,u_i^n)]```

# pour l'inconnue (u_i^n) avec i dans Z et n dans N approchant la valeur
# moyenne de la solution u dans un intervalle de taille dx.
#
# La fonction F(u,v) de R^2 dans R est le flux numérique.
#
# Le schéma est stable sous la condition CFL dt < c*dx où c est la plus
# grande vitesse, que l'on peut prendre par exemple égale à c = max
# |f'(u_0)|.

def f_adv(u):
    """Fonction f pour l'équation de transport à vitesse a"""
    return a*u
def fp_adv(u):
    """Dérivée de f pour l'équation de transport"""
    return a*np.ones_like(u)

def f_b(u):
    """Foncton f pour l'équation de Bürgers"""
    return 0.5*u**2
def fp_b(u):
    """Dérivée de f pour l'équation de Bürgers"""
    return u

# Données initiales possibles à support sur (0,1)
def creneau(x):
    """Fonction créneau entre 0 et 1"""
    return 0.*x + (0.<x)*(x<1.)

def bosse(x):
    """Bosse sinusoidale entre 0 et 1, prolongée par 0 continuement"""
    return 0.*x + (0.<x)*(x<1.)*np.sin(np.pi*x)

a   = 1.0     # vitesse d'advection
f   = f_b     # choix du modèle
fp  = fp_b
u_0 = bosse   # choix de la condition initiale

x0,x1 = 0.,1.     # support données initiale
N     = 50        # nombre de mailles sur (a,b)
dx    = (x1-x0)/N # dx

# Évaluation de la vitesse maximale
c   = np.max( np.abs( fp( u_0( np.arange(x0+0.5*dx,x1,dx) ) ) ) )

# Flux numériques possibles
def F_LF(u,v):
    """Flux de Lax-Friedrichs"""
    return 0.5*(f(u)+f(v)) - 0.5*dx/dt * (v-u)

def F_c(u,v):
    """Flux centré"""
    return f(0.5*(u+v))

F = F_LF      # choix du flux numérique

T = 1.        # temps final
dt = 0.9*c*dx # CFL avec facteur de protection 0.9

# Allocations et initialisation
A,B = x0-c*T,x1+c*T             # intervalle dans lequel la solution
                                # reste à support compact
x = np.arange(A+0.5*dx,B+0.5*dx,dx) # centres de gravités des mailles
tab_t = np.arange(0.,T+dt,dt)   # tableau des temps

nx = x.shape[0]     # Nombre de mailles
nt = tab_t.shape[0] # Nombre de temps

u = np.zeros((nt,nx)) # allocation mémoire pour tous les pas de temps et
                      # tous les x -- peut-être trop
                      
u[0] = u_0(x) # donnée initiale

for n in np.arange(nt-1):
    # Initialisation
    u[n+1] = u[n]
    # Bord gauche
    G = F(0.,u[n,0])
    u[n+1,0] +=  + dt/dx * G
    # Flux
    for i in np.arange(nx-1):
        G = F(u[n,i],u[n,i+1])
        u[n+1,i]   +=  - dt/dx * G
        u[n+1,i+1] +=  + dt/dx * G
    # Bord droit
    G = F(u[n,nx-1],0.)
    u[n+1,nx-1] +=  - dt/dx * G

plt.plot(x,u[0],'r-')
plt.plot(x,u[nt//2],'k:')
plt.plot(x,u[nt-1],'b-')

plt.show()
