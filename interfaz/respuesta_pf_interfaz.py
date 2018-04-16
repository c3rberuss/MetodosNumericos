# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'respuesta_pf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(662, 427)
        Dialog.setModal(True)
        self.tbIteraciones = QtWidgets.QTableWidget(Dialog)
        self.tbIteraciones.setGeometry(QtCore.QRect(10, 180, 641, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbIteraciones.sizePolicy().hasHeightForWidth())
        self.tbIteraciones.setSizePolicy(sizePolicy)
        self.tbIteraciones.setMinimumSize(QtCore.QSize(641, 0))
        self.tbIteraciones.setMaximumSize(QtCore.QSize(641, 192))
        self.tbIteraciones.setObjectName("tbIteraciones")
        self.tbIteraciones.setColumnCount(2)
        self.tbIteraciones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbIteraciones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tbIteraciones.setHorizontalHeaderItem(1, item)
        self.tbIteraciones.horizontalHeader().setDefaultSectionSize(317)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.label.setStyleSheet("font-size: 12px;\n"
"font-style: bold;")
        self.label.setObjectName("label")
        self.btnCerrar = QtWidgets.QPushButton(Dialog)
        self.btnCerrar.setGeometry(QtCore.QRect(570, 390, 85, 29))
        self.btnCerrar.setStyleSheet("background-color: red;\n"
"color: white;")
        self.btnCerrar.setObjectName("btnCerrar")
        self.txtRespuesta = QtWidgets.QTextEdit(Dialog)
        self.txtRespuesta.setGeometry(QtCore.QRect(10, 40, 641, 131))
        self.txtRespuesta.setReadOnly(True)
        self.txtRespuesta.setObjectName("txtRespuesta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Respuesta"))
        item = self.tbIteraciones.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Xn"))
        item = self.tbIteraciones.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Respuesta</span></p></body></html>"))
        self.btnCerrar.setText(_translate("Dialog", "Cerrar"))
        self.txtRespuesta.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

