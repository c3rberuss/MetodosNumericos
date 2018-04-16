# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 382)
        MainWindow.setStyleSheet("background-color: #e1e1e1;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBiseccion = QtWidgets.QPushButton(self.centralwidget)
        self.btnBiseccion.setGeometry(QtCore.QRect(150, 40, 331, 111))
        self.btnBiseccion.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: #FFF;\n"
"font-size: 18px;")
        self.btnBiseccion.setObjectName("btnBiseccion")
        self.btnPuntoFijo = QtWidgets.QPushButton(self.centralwidget)
        self.btnPuntoFijo.setGeometry(QtCore.QRect(150, 170, 331, 111))
        self.btnPuntoFijo.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: #FFF;\n"
"font-size: 18px;\n"
"")
        self.btnPuntoFijo.setObjectName("btnPuntoFijo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 23))
        self.menubar.setObjectName("menubar")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDesarrollador = QtWidgets.QAction(MainWindow)
        self.actionDesarrollador.setObjectName("actionDesarrollador")
        self.menuAcerca_de.addAction(self.actionDesarrollador)
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBiseccion.setText(_translate("MainWindow", "Método de Bisección"))
        self.btnPuntoFijo.setText(_translate("MainWindow", "Método de Punto Fijo"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de"))
        self.actionDesarrollador.setText(_translate("MainWindow", "Desarrollador"))

