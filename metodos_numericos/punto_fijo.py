#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math
from sympy import *
from mpmath import *


def eval_(v_ini, tolerancia, ec):
    i = 1
    N = 1000
    p_cero = float(v_ini)
    p0_ = p_cero
    TOL = float(tolerancia)
    datos = []
    datos_por_iteracion = []
    ecuacion = str(ec)

    g = lambda x, e=math.e: float(eval(str(ecuacion)))

    """ 
    g_prime = lambda ec, x=Symbol('x'): str(diff(eval(ec),x))
    g_prime_eval = lambda x, g_: abs(float(eval(g_)))

    if not (g_prime_eval(p_cero, g_prime(ecuacion)) < 1):
        
        x = Symbol('x')
        ecuacion = str(solve(eval(str(ecuacion))))

        if not (g_prime_eval(p_cero, g_prime(ec)) < 1):
            return False, p, i, p0_, datos
    """
    while i <= N:
        try:
            p = g(p_cero)

            datos_por_iteracion.append(p_cero)
            datos_por_iteracion.append(p)

            datos.append(datos_por_iteracion)
            datos_por_iteracion = []

            if abs(p-p_cero) < TOL:
                return True, p, i, p0_, datos
                break;
                
            p_cero = p

            i+=1 

        except Exception as e:
            return False, p, i, p0_, datos
            
    else:
        return False, p, i, p0_, datos


#print(eval_(3, 1e-10 ,"sqrt( (3*x-1)/x )"))




