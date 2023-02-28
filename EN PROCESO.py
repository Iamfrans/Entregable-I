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
#ventana de Aplicativo
if __name__ == '_main_':
    window = Tk()
    aplication = Product(window)
    window.mainloop()