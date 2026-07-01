from tkinter import *
from figuras import Figuras
class Rabisco(Figuras):
    #primeiro clique do mouse cria o primeiro ponto da linha
    def __init__(self, event):
        self.pontos = []
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
        Figuras.objetos.append(self)
    
    def adicionar_ponto(self, event):
        global canvas
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
        canvas.create_line(self.pontos, fill='black', width=2)
    