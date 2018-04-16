#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
#from PyQt5 import uic
#from PyQt5.QtGui import QIcon

from controladores import biseccion_controlador as bs
from controladores import punto_fijo_controlador as pf
from interfaz import main_interfaz as mi
from interfaz import biseccion_interfaz as bi_in
from interfaz import punto_fijo_interfaz as pf_in

import sys

app = QApplication(sys.argv)

#clase de la Ventana Principal
class MainWindow(QMainWindow):
    
    interfaz = None

    def __init__(self, interfaz_):
        QMainWindow.__init__(self)
        
        self.interfaz = interfaz_

        self.interfaz.setupUi(self)
        #self.setWindowIcon(QIcon("assets/icon.png"))
        self.interfaz.actionDesarrollador.setText("Desarrollo")
        self.interfaz.actionDesarrollador.triggered.connect(self.informacion)

        self.setFixedSize(631,382)

    def informacion(self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Acerca del Desarrollador")
        mensaje.setText("Desarrollador: Josué Amaya - BA16010\n\n")
        mensaje.setInformativeText("Lenguaje: Python 3.5\n"+
                                "Interfaz: Qt5\n"+
                                "Librerías: matplotlib, sympy, PyQt, numpy"
                                +"\n\n@c3rberuss")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()


main_interface = mi.Ui_MainWindow()
ventana = MainWindow(main_interface)

ventana.setWindowTitle("Análisis Numérico")

biseccion = bs.Biseccion(bi_in.Ui_Dialog())
punto_fijo = pf.PuntoFijo(pf_in.Ui_Dialog())

ventana.interfaz.btnBiseccion.clicked.connect(biseccion.exec_)
ventana.interfaz.btnPuntoFijo.clicked.connect(punto_fijo.exec_)

ventana.show()
app.exec_()