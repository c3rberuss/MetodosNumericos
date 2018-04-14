#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from controladores import biseccion_controlador as bs
from controladores import punto_fijo_controlador as pf

import sys

app = QApplication(sys.argv)

#clase de la Ventana Principal
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("interfaz/main.ui", self)

        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setFixedSize(631,382)
        
ventana = MainWindow()
biseccion = bs.Biseccion()
punto_fijo = pf.PuntoFijo()

ventana.setWindowTitle("Análisis Numérico")
ventana.btnBiseccion.clicked.connect(biseccion.exec_)
ventana.btnPuntoFijo.clicked.connect(punto_fijo.exec_)

ventana.show()
app.exec_()