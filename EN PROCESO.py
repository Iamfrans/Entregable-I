#diseño de interfaz
from tkinter import ttkthemes
from tkinter import *

import sqlite3
#creamos class product para agregar, eliminar, editar productos
class Product:
    def __init__(self, window):
        self.wind = window 
