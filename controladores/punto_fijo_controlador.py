from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog
from PyQt5 import uic
from metodos_numericos import punto_fijo as pf
from controladores import respuesta_punto_fijo_controlador as res
from matplotlib import pyplot
from sympy import *

import numpy as np
import math

"""def e_(exponente):
    return math.exp(exponente)

def exp_(x, expo):
    return math.pow(x, expo)

def raiz_(x, expo=2):
    return exp(x, 1/expo)

def cos_(x):
    return math.cos(x)

def sen_(x):
    return math.sin(x)

def tan_(x):
    return math.tan(x)"""

class PuntoFijo(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("interfaz/punto_fijo.ui", self)

        self.message = QMessageBox(self)

        self.setFixedSize(633, 466)

        #eventos de Botones
        self.btnCerrar.clicked.connect(self.close_)
        self.btnRaiz.clicked.connect(self.add_raiz)
        self.btnExponente.clicked.connect(self.add_exponente)
        self.btnParentesis.clicked.connect(self.add_parentesis)
        self.btnCos.clicked.connect(self.add_cos)
        self.btnSen.clicked.connect(self.add_sen)
        self.btnTan.clicked.connect(self.add_tan)
        self.btnMas.clicked.connect(self.add_mas)
        self.btnMenos.clicked.connect(self.add_menos)
        self.btnPor.clicked.connect(self.add_por)
        self.btnEntre.clicked.connect(self.add_entre)
        self.btnPi.clicked.connect(self.add_pi)
        self.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.btnX.clicked.connect(self.add_x)
        self.btnGraficar.clicked.connect(self.graficar)
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnEF.clicked.connect(self.add_ef)
        self.btnLn.clicked.connect(self.add_ln)
        self.btnLog.clicked.connect(self.add_log)
        
        self.txtEcuacion.textChanged.connect(self.actualizar_eq)
        #self.btnVer.clicked.connect(self.actualizar_eq)

        #placeholders
        self.txtEcuacion.setPlaceholderText("Pow( x,2 ) + (3*x) - 1")
        self.txtVInicial.setPlaceholderText("1")
        self.txtTolerancia.setPlaceholderText("1e-8")


    def actualizar_eq(self):
        try:
            x = Symbol('x')
            y = eval(self.txtEcuacion.toPlainText())
        
            eq = pretty(y)

            if not "<class" in eq and not "<func" in eq:
                self.txtEcuacionR.setPlainText(eq)

        except Exception as e:
            self.txtEcuacionR.setPlainText("")

    def mostra_respuesta(self, response, ec):
        if response[0]:
            resp = res.Resp(response, ec)
            resp.exec_()
        else:
            self.mensaje("Infomación", "Informativo", "La ecuación f(x) = "+str(ec)+"\n\n"+
                        "Se vuelve inestable, pruebe con reescribiendo la ecuación.")

    def close_(self):
        self.limpiar_campos()
        self.close()
    
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
            x = np.arange(float(eval(data[0])), float(eval(data[1])), 0.01)
            x2 = np.arange(-60.0,60.0,0.01)
            # Graficar ambas funciones.

            try:
                self.mensaje("Graficando...", "Informativo", "Espere un momento mientras se genera la gráfica.\n"+
                "Esto puede tardar un poco, ten paciencia.")

                gx = lambda x, e=math.e: float(eval(str(self.txtEcuacion.toPlainText())))
                fx = lambda x: x

                pyplot.plot(x, [gx(i) for i in x])
                pyplot.plot(x2, [fx(i) for i in x2])

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
                eq = latex(eval(self.txtEcuacion.toPlainText()))
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

    def add_raiz(self):

        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("sqrt(  )")
        else:
            cursor.insertText("sqrt( "+cursor.selectedText()+" )")

    def add_parentesis(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("(  )")
        else:
            cursor.insertText("( "+cursor.selectedText()+" )")

    def add_x(self):
        cursor = self.txtEcuacion.textCursor()

        cursor.insertText("x")
    
    def add_exponente(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("Pow( x, exponente )")
        else:
            cursor.insertText("Pow( "+cursor.selectedText()+" )")

    def add_cos(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("cos( x )")
        else:
            cursor.insertText("cos( "+cursor.selectedText()+" )")

    def add_sen(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("sin( x )")
        else:
            cursor.insertText("sin( "+cursor.selectedText()+" )")

    def add_ln(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("ln( x )")
        else:
            cursor.insertText("ln( "+cursor.selectedText()+" )")

    def add_log(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("log( x, base )")
        else:
            cursor.insertText("log( "+cursor.selectedText()+" )")

    def add_ef(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("exp( x )")
        else:
            cursor.insertText("exp( "+cursor.selectedText()+" )")

    def add_tan(self):
        cursor = self.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("tan( x )")
        else:
            cursor.insertText("tan( "+cursor.selectedText()+" )")
    
    def add_mas(self):
        cursor = self.txtEcuacion.textCursor()

        cursor.insertText("+")

    def add_menos(self):
        cursor = self.txtEcuacion.textCursor()

        cursor.insertText("-")
    
    def add_por(self):
        cursor = self.txtEcuacion.textCursor()

        cursor.insertText("*")

    def add_entre(self):
        cursor = self.txtEcuacion.textCursor()

        cursor.insertText("/")

    def add_pi(self):
        cursor = self.txtEcuacion.textCursor()
        cursor.insertText("pi")

    def limpiar_campos(self):
        self.txtEcuacion.setPlainText("")
        self.txtEcuacionR.setPlainText("")
        self.txtVInicial.clear()
        self.txtTolerancia.clear()

    def calcular(self):
        inicial = self.txtVInicial.text()
        tol = self.txtTolerancia.text()
        ec = self.txtEcuacion.toPlainText()

        try:
            respuesta = pf.eval_(inicial, tol, ec)
            #print(respuesta)
            self.mostra_respuesta(respuesta, ec)

        except Exception as e:
            self.mensaje("Advertencia", "Advertencia", "Los parámetros para encontrar la raíz son incorrectos.", e)

    def mensaje(self, titulo:str, icono: str, texto:str, Error="*"):
        self.message.setWindowTitle(titulo)

        if icono == "Informativo":
            self.message.setIcon(QMessageBox.Information)
        elif icono == "Error":
            self.message.setInformativeText("Error: "+str(Error))
            self.message.setIcon(QMessageBox.Critical)
        elif icono == "Advertencia":
            self.message.setIcon(QMessageBox.Warning)
            self.message.setInformativeText("Información: "+str(Error))
        elif icono == "Pregunta":
            self.message.setIcon(QMessageBox.Question)
        elif icono == "No":
            self.message.setIcon(QMessageBox.NoIcon)
        
        self.message.setText(texto)

        self.message.exec_()