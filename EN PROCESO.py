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
#ingreso de Botones
btn1 = Button(ventana, text="Agregar",
        font=("Arial", 12), width=10,
        command=funAgregar)
btn1.place(x=10, y=220)

btn2 = Button(ventana, text="Consultar",
        font=("Arial", 12), width=10,
        command=funConsultar)
btn2.place(x=110, y=220)

btn3 = Button(ventana, text="Modificar",
        font=("Arial", 12), width=10,
        command=funModificar)
btn3.place(x=210, y=220)

btn4 = Button(ventana, text="Eliminar",
        font=("Arial", 12), width=10,
        command=funEliminar)
btn4.place(x=310, y=220)

btn5 = Button(ventana, text="Ejecutar",
        font=("Arial", 12), width=10,
        command=funEjecutar)
btn5.place(x=10, y=300)

btn6 = Button(ventana, text="Salir",
        font=("Arial", 12), width=10,
        command = funsalir)

btn6.place(x=110, y=300)


ventana.mainloop()
