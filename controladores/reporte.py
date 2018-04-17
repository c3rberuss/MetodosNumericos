#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

doc_save_path = os.getcwd()

if not os.path.exists(doc_save_path+"/prueba"):
    os.mkdir(doc_save_path+"/prueba")

doc = SimpleDocTemplate(doc_save_path+"/prueba/simple_table_grid3.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
data= [['00', '01', '02', '03', '04'],
       ['10', '11', '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]

t=Table(data,5*[0.4*inch], 4*[0.4*inch])

t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),

                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
 
elements.append(t)
# write the document to disk
doc.build(elements)"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.pdfgen import textobject
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
import os

 

"""P0 = Paragraph('''
               <b>A pa<font color=red>r</font>a<i>graph</i></b>
               <super><font color=yellow>1</font></super>''',
               styleSheet["BodyText"])

P = Paragraph('''
    <para align=center spaceb=3>The <b>ReportLab Left
    <font color=red>Logo</font></b>
    Image</para>''',
    styleSheet["BodyText"])"""

"""data= [['A', 'B', 'C', P0, 'D'],
       ['00', '01', '02', [P], '04'],
       ['10', '11', '12', [P], '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', '33', '34']]
 
t=Table(data,style=[('GRID',(1,1),(-2,-2),1,colors.green),
                    ('BOX',(0,0),(1,-1),2,colors.red),
                    ('LINEABOVE',(1,2),(-2,2),1,colors.blue),
                    ('LINEBEFORE',(2,1),(2,-2),1,colors.pink),
                    ('BACKGROUND', (0, 0), (0, 1), colors.pink),
                    ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
                    ('BACKGROUND', (2, 2), (2, 3), colors.orange),
                    ('BOX',(0,0),(-1,-1),2,colors.black),
                    ('GRID',(0,0),(-1,-1),0.5,colors.black),
                    ('VALIGN',(3,0),(3,0),'BOTTOM'),
                    ('BACKGROUND',(3,0),(3,0),colors.limegreen),
                    ('BACKGROUND',(3,1),(3,1),colors.khaki),
                    ('ALIGN',(3,1),(3,1),'CENTER'),
                    ('BACKGROUND',(3,2),(3,2),colors.beige),
                    ('ALIGN',(3,2),(3,2),'LEFT'),
])
t._argW[3]=1.5*inch
 
elements.append(t)
# write the document to disk
doc.build(elements)
"""
class saveReport():

    ecuacion = None
    intervalos = None
    tolerancia = None
    raiz = None
    data = None
    metodo = None
    iteraciones = None
    path_biseccion = os.getcwd()+"/Soluciones/Biseccion"
    path_punto_fijo = os.getcwd()+"/Soluciones/Punto_Fijo"

    def __init__(self, eq, inter, tol, raiz_, data_, met, itera):
        self.ecuacion = eq
        self.intervalos = inter
        self.tolerancia = tol
        self.raiz = raiz_
        self.data = data_
        self.metodo = met
        self.iteraciones = itera

        self.crear_carpeta()
        self.crear_carpeta()

    def crear_pdf_biseccion(self):

        header = None

        titulo = "Ec_"+self.ecuacion+"_Int_"+str(self.intervalos)+"_Tol_"+self.tolerancia

        if self.metodo == "Biseccion":
            header = "f(x) = "+ self.ecuacion
            titulo = "Soluciones/Biseccion/"+titulo
        else:
            header = "g(x) = "+ self.ecuacion
            titulo = "Soluciones/Punto_Fijo/"+titulo

        doc = SimpleDocTemplate(titulo+".pdf", pagesize=landscape(letter))
        elements = []

        styleSheet = getSampleStyleSheet()


        header_ = Paragraph("<b><font color=red >Método de "+self.metodo+"</font></b>", styleSheet['Heading1'])
        texto1 = Paragraph("<b>La Ecuación <font color=red>"+header+"</font></b>", styleSheet['Heading2'])
        texto2 = Paragraph("<b>Tiene una Raiz <font color=red>x = "+self.raiz+"</font></b>", styleSheet['Heading2'])
        texto3 = Paragraph("<b>En el intervalo <font color=red>"+str(self.intervalos)+"</font></b>", styleSheet['Heading2'])
        texto4 = Paragraph("<b>Con tolerancia <font color=red>"+str(self.tolerancia)+"</font></b>", styleSheet['Heading2'])
        texto5 = Paragraph("<b>Tardó <font color=red>"+str(self.iteraciones)+"</font> iteraciones en encontrar dicha raíz.</b>", styleSheet['Heading2'])

        elements.append(header_)
        elements.append(texto1)
        elements.append(texto2)
        elements.append(texto3)
        elements.append(texto4)
        elements.append(texto5)
        elements.append(Paragraph("",styleSheet['Heading1']))

        self.data.insert(0, (Paragraph("<b><font color=white>n</font></b>", styleSheet["Heading2"]), Paragraph("<b><font color=white>a</font></b>",styleSheet["Heading2"]), 
                            Paragraph("<b><font color=white>b</font></b>",styleSheet["Heading2"]), Paragraph("<b><font color=white>p</font></b>",styleSheet["Heading2"]), 
                            Paragraph("<b><font color=white>f(p)</font></b>",styleSheet["Heading2"])))
        
        
        for i in range(1,len(self.data),1):
            self.data[i].insert(0,i)

        t=Table(self.data,style=[
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('BACKGROUND', (0, 0), (0, -1), colors.blue),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                    ('TEXTCOLOR',(0,0),(0,-1),colors.white),
                    ('SIZE', (0,0), (-1,-1), 15),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.red),
                    ('SIZE', (1,1),(-1,-1), 12)
        ])

        t._argW[0]=0.6*inch
        t._argW[1]=1.9*inch
        t._argW[2]=1.9*inch
        t._argW[3]=1.9*inch
        t._argW[4]=2.5*inch

        for i in range(len(self.data)):
            t._argH[i]=0.4*inch
        

        elements.append(t)
        # write the document to disk
        doc.build(elements)


    def crear_carpeta(self):
        
        if not os.path.exists(os.getcwd()+"/Soluciones"):
            os.mkdir(os.getcwd()+"/Soluciones")
            os.mkdir(self.path_biseccion)
            os.mkdir(self.path_punto_fijo)

    def crear_pdf_punto(self):
    
        header = None

        titulo = "Ec_"+self.ecuacion+"_Xi_"+str(self.intervalos)+"_Tol_"+self.tolerancia

        if self.metodo == "Biseccion":
            header = "f(x) = "+ self.ecuacion
            titulo = "Soluciones/Biseccion/"+titulo
        else:
            header = "g(x) = "+ self.ecuacion
            titulo = "Soluciones/Punto_Fijo/"+titulo

        doc = SimpleDocTemplate(titulo+".pdf", pagesize=landscape(letter))
        elements = []

        styleSheet = getSampleStyleSheet()


        header_ = Paragraph("<b><font color=red >Método de "+self.metodo+"</font></b>", styleSheet['Heading1'])
        texto1 = Paragraph("<b>La Ecuación <font color=red>"+header+"</font></b>", styleSheet['Heading2'])
        texto2 = Paragraph("<b>Tiene una Raiz <font color=red>x = "+self.raiz+"</font></b>", styleSheet['Heading2'])
        texto3 = Paragraph("<b>Valor Inicial  <font color=red> X1 ="+str(self.intervalos)+"</font></b>", styleSheet['Heading2'])
        texto4 = Paragraph("<b>Con tolerancia <font color=red>"+str(self.tolerancia)+"</font></b>", styleSheet['Heading2'])
        texto5 = Paragraph("<b>Tardó <font color=red>"+str(self.iteraciones)+"</font> iteraciones en encontrar dicha raíz.</b>", styleSheet['Heading2'])

        elements.append(header_)
        elements.append(texto1)
        elements.append(texto2)
        elements.append(texto3)
        elements.append(texto4)
        elements.append(texto5)
        elements.append(Paragraph("",styleSheet['Heading1']))

        self.data.insert(0, (Paragraph("<b><font color=white>n</font></b>", styleSheet["Heading2"]), Paragraph("<b><font color=white>Xn</font></b>",styleSheet["Heading2"]), 
                            Paragraph("<b><font color=white>X</font></b>",styleSheet["Heading2"])))
        
        
        for i in range(1,len(self.data),1):
            self.data[i].insert(0,i)

        t=Table(self.data,style=[
                    ('GRID',(0,0),(-1,-1),1,colors.black),
                    ('BACKGROUND', (0, 0), (0, -1), colors.blue),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                    ('TEXTCOLOR',(0,0),(0,-1),colors.white),
                    ('SIZE', (0,0), (-1,-1), 15),
                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.red),
                    ('SIZE', (1,1),(-1,-1), 12)
        ])

        t._argW[0]=0.6*inch
        t._argW[1]=2.5*inch
        t._argW[2]=2.5*inch

        for i in range(len(self.data)):
            t._argH[i]=0.4*inch
        

        elements.append(t)
        # write the document to disk
        doc.build(elements)

