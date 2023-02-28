#diseño de interfaz
from tkinter import ttkthemes
from tkinter import *

import sqlite3
#creamos class product para agregar, eliminar, editar productos
class Product:
    def __init__(self, window):
        self.wind = window 
#Le damos el titulo 
        self.wind.title('Ferreteria: El baul de Anonymous')
 #creando cuadro para agregar elemnto 
        DNI = LabelFrame(self.wind, text='')
        DNI.grit(row = 0 columm = 0, columnspan = 3, pady = 28)

        label(frame, Text = 'DNI: ').grit(row = 1, column = 0)
        self.name = Entry(Frame)
        self.name.grid(row = 1, column =1)
#ventana de Aplicativo
if __name__ == '_main_':
    window = Tk()
    aplication = Product(window)
    window.mainloop()