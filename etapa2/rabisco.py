from tkinter import *
from figuras import Figuras
class Rabisco(Figuras):
    def __init__(self, event, fill="black", outline="black"):
        self.ini_x = event.x
        self.ini_y = event.y
        self.fim_x = event.x
        self.fim_y = event.y
        self.pontos = []
        self.fill = fill
        self.outline = outline
    
    def atualizar_coordenadas(self,event, canvas):
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
        canvas.create_line(self.pontos, fill=self.fill, dash=(4,2))
    
    def desenhar_figura(self, canvas):
        canvas.create_line(self.pontos, fill=self.fill)
    
    def esta_incompleta(self):
        return len(self.pontos) <= 1