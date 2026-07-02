from tkinter import *
from figuras import Figuras
class Rabisco(Figuras):
    #primeiro clique do mouse cria o primeiro ponto da linha
    def __init__(self, event, fill, outline):
        super().__init__(event, fill, outline)
        self.pontos = []
        self.pontos.append((self.ini_x, self.ini_y))
    
    def atualizar_coordenadas(self,event, canvas):
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
        canvas.create_line(self.pontos, fill=self.fill, width=2, dash=(4,2))
    
    def desenhar_figura(self, canvas):
        canvas.create_line(self.pontos, fill=self.fill, width=2)
    
    def esta_incompleta(self):
        return len(self.pontos) <= 1