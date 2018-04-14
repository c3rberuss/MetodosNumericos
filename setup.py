from setuptools import setup, find_packages

import os

setup(
    name = "Análisis Numérico",
    version = "0.0.4",
    author = "Josué Amaya - @c3rberuss_",
    author_email = "c3rberuss@gmail.com",
    description = ("Implementación de los algoritmos de los método numéricos siguientes: Método de Bisección, Método de punto fijo"),
    keywords = "analisis metodo numerico biseccion punto fijo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.5"
    ],
    install_requires = ['PyQt5', 'matplotlib', 'numpy', 'sympy', 'scipy']
)