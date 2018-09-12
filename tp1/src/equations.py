#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Fonction f(t,y), second membre d'équations différentielles d'ordre 1
# écrite sous la forme d'un problème de Cauchy, y'(t) = f(t,y(t)) avec
# y(0)=y0

a = -1.
b = 1.

def f_affine(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a*y+b
def sol_affine(t,y0):
    """Pour une fonction affine, on connait la solution exacte. C'est
    y(t0+s) = y0*exp(a*s) - b*(1-exp(a*s))/a, soit y(t) =
    y0*exp(a*(t-t0)) - b*(1-exp(a*(t-t0)))/a

    """
    t0 = t[0]
    return y0*np.exp(a*(t-t0)) - b * (1.-np.exp(a*(t-t0)))/a
