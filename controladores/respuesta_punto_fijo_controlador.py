from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic

class Resp(QDialog):
    
    interfaz = None

    def __init__(self, response, ec, interfaz_):
        QDialog.__init__(self)
        #uic.loadUi("interfaz/respuesta_pf.ui", self)
        self.interfaz = interfaz_
        self.interfaz.setupUi(self)
        self.interfaz.btnCerrar.clicked.connect(self.close)

        self.interfaz.txtRespuesta.insertHtml("<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+
        "<span style=\" font-size:12pt;\"> La ecuación </span><span style=\" font-size:12pt; font-weight:600;\"> f(x) = "+str(ec)+"</span> <br><br> <span style=\" font-size:12pt;\">Tiene raíz en </span><span style=\" font-size:12pt; font-weight:600;\"> x = "+str(response[1])+"</span>"+
       ".<br><br>"+"<span style=\" font-size:12pt;\">Para encontrar dicha raíz fue necesario realizar </span> <span style=\" font-size:12pt; font-weight:600;\">"+str(response[2])+"</span> <span style=\" font-size:12pt;\">iteraciones.</span>"+
        "<p>")
        
        self.interfaz.tbIteraciones.setRowCount(0)
        for row in range(len(response[4])):
            self.interfaz.tbIteraciones.insertRow(row)
            for columns in range(2):
                item = str(response[4][row][columns])
                self.interfaz.tbIteraciones.setItem(row,columns, QTableWidgetItem(item))
