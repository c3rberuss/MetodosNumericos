#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math
from sympy import *
from mpmath import pi, euler

"""def e_(exponente):
    return math.exp(exponente)

def exp(x, expo):
    return math.pow(x, expo)

def raiz(x, expo=2):
    return exp(x, 1/expo)

def cos(x):
    return math.cos(x)

def sen(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)"""

def eval_(inferior, superior, tolerancia, ec):
    i = 1
    N = 1000
    inf = float(eval(inferior))
    sup = float(eval(superior))
    p = 0
    TOL = float(tolerancia)
    datos = []
    datos_por_iteracion = []
    ecuacion = str(ec)

    a_ = inf
    b_ = sup

    f = lambda x, e=math.e: float(eval(ecuacion))

    FA = f(inf)
    FP = 0

    if not (f(inf)*f(sup) < 0):
        return False, p, i, a_, b_, datos

    while i <= N:
        p = inf + (sup-inf)/2
        FP = f(p)

        datos_por_iteracion.append(inf)
        datos_por_iteracion.append(sup)

        datos_por_iteracion.append(p)
        datos_por_iteracion.append(FP)

        datos.append(datos_por_iteracion)
        datos_por_iteracion = []

        if(FP == 0 or ((sup-inf)/2) < TOL):
            return True, p, i, a_, b_, datos
            break;
        
        i+=1

        if(FA*FP > 0):
            inf = p
            FA = FP
        else:
            sup = p

    else:
        return False, p, i, a_, b_, datos


#res = eval_(1, 2, 1e-8, "(math.pow(x,3)+(4*math.pow(x,2))-10)")
#print(res[0], res[2][1][1], res[2][1][2], res[2][1][3], res[2][1][0], res[2][1][4])
