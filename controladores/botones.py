from PyQt5.QtWidgets import QMessageBox

class Acciones():

    def add_raiz(self):
    
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("sqrt(  )")
        else:
            cursor.insertText("sqrt( "+cursor.selectedText()+" )")

    def add_parentesis(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("(  )")
        else:
            cursor.insertText("( "+cursor.selectedText()+" )")

    def add_x(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        cursor.insertText("x")
    
    def add_exponente(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("Pow( x, exponente )")
        else:
            cursor.insertText("Pow( "+cursor.selectedText()+" )")

    def add_cos(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("cos( x )")
        else:
            cursor.insertText("cos( "+cursor.selectedText()+" )")

    def add_sen(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("sin( x )")
        else:
            cursor.insertText("sin( "+cursor.selectedText()+" )")

    def add_ln(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("ln( x )")
        else:
            cursor.insertText("ln( "+cursor.selectedText()+" )")

    def add_log(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("log( x, base )")
        else:
            cursor.insertText("log( "+cursor.selectedText()+" )")

    def add_ef(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("exp( x )")
        else:
            cursor.insertText("exp( "+cursor.selectedText()+" )")

    def add_tan(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        if cursor.selectedText() == "":
            cursor.insertText("tan( x )")
        else:
            cursor.insertText("tan( "+cursor.selectedText()+" )")
    
    def add_mas(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        cursor.insertText("+")

    def add_menos(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        cursor.insertText("-")
    
    def add_por(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        cursor.insertText("*")

    def add_entre(self):
        cursor = self.interfaz.txtEcuacion.textCursor()

        cursor.insertText("/")

    def add_pi(self):
        cursor = self.interfaz.txtEcuacion.textCursor()
        cursor.insertText("pi")

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

    def close_(self):
        self.limpiar_campos()
        self.close()
    