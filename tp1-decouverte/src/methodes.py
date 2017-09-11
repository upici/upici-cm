#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def euler_explicite(t0,h,N, y0,f):
    """Méthode d'Euler pour la résolution d'un problème de Cauchy.

    Resolution de y'(t) = f(t,y(t)) avec y(t0) = y0 par la méthode d'Euler
    explicite avec un pas de temps h>0 et pour t = k*h, k=0..N.

    """

    t = np.arange(t0,t0+N*h,h)
    y = 0.*t # Alloue un tableau de la taille de t, initialisé à 0.

    # Donnée initiale
    y[0] = y0

    # Itérations en temps
    for k in np.arange(0,N-1,1):
        y[k+1] = y[k] + h*f(t[k],y[k])

    return [t,y]

