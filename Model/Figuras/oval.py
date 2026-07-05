from tkinter import *
from .figuras import Figuras

class Oval(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y)

    def desenhar_figura_pontilhada(self, canvas):
        canvas.create_oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline, width=self.width, dash=(4, 2))

    def desenhar_figura(self, canvas):
        canvas.create_oval(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline, width=self.width)