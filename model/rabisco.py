from tkinter import *
from figuras import Figuras
from control import Desenhar

class Rabisco(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
        self.pontos = [(event.x, event.y)]
    
    #Atualiza as coordenadas do ponto final da figura, adicionando o ponto à lista de pontos
    def atualizar_coordenadas(self,event, canvas):
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
        if len(self.pontos) >= 2:
            canvas.create_line(self.pontos, fill=self.fill, width=self.width, dash=(4,2))
    
    #Desenha a figura pontilhada no canvas
    def desenhar_figura(self, canvas):
        canvas.create_line(self.pontos, fill=self.fill, width=self.width)
    
    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def esta_incompleta(self):
        return len(self.pontos) <= 1