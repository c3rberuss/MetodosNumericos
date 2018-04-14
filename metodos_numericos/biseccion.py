import math

inferior = 0.0
superior = 0.0
ecuacion = ""
tolerancioa = 0.0
resultado = 0.0
x = 0.0

def exp(x, expo):
    return math.pow(x, expo)

def raiz(x, expo=2):
    return exp(x, 1/expo)

def cos(x):
    return math.cos(x)

def sen(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)

def firstStep(ecu, a, b):
    
    global x

    x = a
    funcA = float(eval(ecu))
    print("paso 1: FuncA = %f"%(funcA))

    x = b
    funcB = float(eval(ecu))
    print("paso 1: FuncB = %f"%(funcB))

    if funcA*funcB < 0:
        print("Respuesta paso 1: True")
        return True
    
    print("Respuesta paso 1: False")
    return False

def secondStep(a, b):
    res = float((a + b) / 2)
    print("Respuesta paso 2: %f" %(res))
    return res



def thirdStep(ecu, a, xr):
    
    global x
    global superior
    global inferior
    global resultado

    x = a
    funcA = float(eval(ecu))
    print("paso 3: FuncA = %f"%(funcA))

    x = xr
    funcXr = float(eval(ecu))
    print("paso 3: FuncA = %f"%(funcA))

    if float(funcA*funcXr) < 0.0:
        print("valor inicial de superior -> %f"%(superior))
        superior = xr
        print("valor actual de superior -> %f"%(superior))
        return False

    elif float(funcA*funcXr) > 0.0:
        print("valor inicial de inferior -> %f"%(inferior))
        inferior = xr
        print("valor actual de inferior -> %f"%(inferior))
        return False
        
    elif float(funcA*funcXr) == 0.0 :
        resultado = xr
        return True

def eval_(a, b, ec, tol):
    
    global inferior 
    inferior = float(a)
    global superior 
    superior = float(b)
    global ecuacion
    ecuacion = str(ec)
    global tolerancioa
    tolerancioa = float(tol)

    if firstStep(ecuacion, inferior, superior):
        
        finalizado = False

        while not finalizado:
            p = secondStep(inferior, superior)
            print(p)
            finalizado = thirdStep(ecuacion, inferior, p)

        #print("Resultado: x = %f"%(resultado))
        print(float(resultado))
        return float(resultado)

    else: 
        print("La Ecucación %s no tiene Raices."%(ecuacion))