from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog
from PyQt5 import uic
from metodos_numericos import biseccion_ as mn
from controladores import Respuesta_biseccion_controlador as res
from matplotlib import pyplot
from sympy import *
from interfaz import respuesta_biseccion_interfaz as res_bi

from controladores.botones import Acciones
import numpy as np
import math


"""def sqrt(numero, raiz=2):
    return float(math.sqrt(float(eval(str(numero)))))"""

"""def e_(exponente):
    return math.exp(exponente)

def exp_(x, expo):
    return math.pow(x, expo)


def cos_(x):
    return math.cos(x)

def sen_(x):
    return math.sin(x)

def tan_(x):
    return math.tan(x)"""

class Biseccion(QDialog, Acciones):

    interfaz = None

    def __init__(self, interfaz_):
        QDialog.__init__(self)
        #uic.loadUi("interfaz/biseccion.ui", self)
        self.interfaz = interfaz_

        self.interfaz.setupUi(self)

        self.message = QMessageBox(self)

        self.setFixedSize(633, 466)

        #eventos de Botones
        self.interfaz.btnCerrar.clicked.connect(self.close_)
        self.interfaz.btnRaiz.clicked.connect(self.add_raiz)
        self.interfaz.btnExponente.clicked.connect(self.add_exponente)
        self.interfaz.btnParentesis.clicked.connect(self.add_parentesis)
        self.interfaz.btnCos.clicked.connect(self.add_cos)
        self.interfaz.btnSen.clicked.connect(self.add_sen)
        self.interfaz.btnTan.clicked.connect(self.add_tan)
        self.interfaz.btnMas.clicked.connect(self.add_mas)
        self.interfaz.btnMenos.clicked.connect(self.add_menos)
        self.interfaz.btnPor.clicked.connect(self.add_por)
        self.interfaz.btnEntre.clicked.connect(self.add_entre)
        self.interfaz.btnPi.clicked.connect(self.add_pi)
        self.interfaz.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.interfaz.btnX.clicked.connect(self.add_x)
        self.interfaz.btnGraficar.clicked.connect(self.graficar)
        self.interfaz.btnCalcular.clicked.connect(self.calcular)
        self.interfaz.btnEF.clicked.connect(self.add_ef)
        self.interfaz.btnLn.clicked.connect(self.add_ln)
        self.interfaz.btnLog.clicked.connect(self.add_log)
        
        self.interfaz.txtEcuacion.textChanged.connect(self.actualizar_eq)
        #self.btnVer.clicked.connect(self.actualizar_eq)

        #placeholders
        self.interfaz.txtEcuacion.setPlaceholderText("f(x) = Pow( x,2 ) + (3*x) - 1")
        self.interfaz.txtSuperior.setPlaceholderText("2")
        self.interfaz.txtInferior.setPlaceholderText("1")
        self.interfaz.txtTolerancia.setPlaceholderText("1e-8")


    def mostra_respuesta(self, response, ec):
        if response[0]:
            resp = res.Resp(response, ec, res_bi.Ui_Dialog())
            resp.exec_()
        else:
            self.mensaje("Infofrom matplotlib import pyplotrmación", "Informativo", "La ecuación f(x) = "+str(ec)+"\n\n"+
                        "No posee ninguna Raíz en el intervalo ["+str(response[3])+","+
                        str(response[4])+"].")
    
    def graficar(self):
        # Valores del eje X que toma el gráfico.

        input_ = QInputDialog(self)
        input_.setLabelText("Ingrese los límites para graficar. \nEj: -10,10")
        input_.setOkButtonText("Graficar")
        input_.setCancelButtonText("Cancelar")
        input_.exec_()

        data = input_.textValue()
        data = data.split(',')

        if(len(data) == 2 and sympify(data[0]).is_real and sympify(data[1]).is_real):
            #x = np.arange(-60.0, 60.0, 0.01)
            x = np.arange(float(eval(data[0])), float(eval(data[1])), 0.1)
            # Graficar ambas funciones.

            try:
                self.mensaje("Graficando...", "Informativo", "Espere un momento mientras se genera la gráfica.\n"+
                "Esto puede tardar un poco, ten paciencia.")

                fx = lambda x, e=math.e: float(eval(self.interfaz.txtEcuacion.toPlainText()))

                pyplot.plot(x, [fx(i) for i in x])

                # Establecer el color de los ejes.
                pyplot.grid(True)
                pyplot.axhline(0, color="black")
                pyplot.axvline(0, color="black")
                # Limitar los valores de los ejes.
                pyplot.xlim(-20, 60)
                pyplot.ylim(-20, 60)
                # Guardar gráfico como imágen PNG.
                #pyplot.savefig("output.png")
            
                x = Symbol('x')
                eq = latex(eval(self.interfaz.txtEcuacion.toPlainText()))
                eq = '$'+eq+'$'
                pyplot.title(r'f(x) = %s'%(eq), fontsize=16)
                pyplot.xlabel("x")
                pyplot.ylabel("y")

                # Mostrarlo.
                pyplot.show()

            except Exception as e:
                self.mensaje("Error", "Error", "Al parecer algo ha salido mal :(",e)            
        else:
            if input_.textValue() != '': 
                self.mensaje("Advertencia", "Advertencia", "Intérvalos incorrectos.",e)

    def calcular(self):
        a = self.interfaz.txtInferior.text()
        b = self.interfaz.txtSuperior.text()
        tol = self.interfaz.txtTolerancia.text()
        ec = self.interfaz.txtEcuacion.toPlainText()

        try:
            respuesta = mn.eval_(a, b, tol, ec)
            #print(respuesta)

            self.mostra_respuesta(respuesta, ec)
        except Exception as e:
            self.mensaje("Advertencia", "Advertencia", "Los parámetros para encontrar la raíz son incorrectos.", e)

    def limpiar_campos(self):
        self.interfaz.txtEcuacion.setPlainText("")
        self.interfaz.txtEcuacionR.setPlainText("")
        self.interfaz.txtSuperior.clear()
        self.interfaz.txtInferior.clear()
        self.interfaz.txtTolerancia.clear()
    
    def actualizar_eq(self):
        try:
            x = Symbol('x')
            y = eval(self.interfaz.txtEcuacion.toPlainText())
        
            eq = pretty(y)
            if not "<class" in eq and not "<func" in eq:
                self.interfaz.txtEcuacionR.setPlainText(eq)

        except Exception as e:
            self.interfaz.txtEcuacionR.setPlainText("")