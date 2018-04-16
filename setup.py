import sys
from cx_Freeze import setup, Executable


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Análisis Numérico",
    version = "0.0.1",
    author = "Josué Amaya - @c3rberuss_",
    author_email = "c3rberuss@gmail.com",
    description = ("Implementación de los algoritmos de los método numéricos siguientes: Método de Bisección, Método de punto fijo"),
    keywords = "analisis metodo numerico biseccion punto fijo",
    executables = [Executable("main.pyw", base=base)]    
    )
