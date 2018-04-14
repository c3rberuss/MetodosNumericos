#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math

def eval_(inferior, superior, tolerancia, ec):
    i = 1
    N = 120
    a = float(inferior)
    b = float(superior)
    p = 0
    TOL = float(tolerancia)
    datos = []

    ecuacion = str(ec)

    f = lambda x, e=math.e: float(eval(ecuacion))

    FA = f(a)
    FP = 0

    while i <= N:
        p = a + (b-a)/2
        FP = f(p)

        if(FP == 0 or ((b-a)/2) < TOL):
            return p, i
            break;
        
        i+=1

        if(FA*FP > 0):
            a = p
            FA = FP
        else:
            b = p

    else:
        print("El método fracasó después de N iteraciones")

print(eval_(1, 2, 1e-8, "(math.pow(x,3)+(4*math.pow(x,2))-10)"))