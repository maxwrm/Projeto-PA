from tkinter import *
from .figuras import Figuras

class Circulo(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y)

    #Calcula o raio do circulo
    def calcular_raio(self):
        return ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
    
    #Desenha a figura pontilhada no canvas
    def desenhar_figura_pontilhada(self, canvas):
        raio = self.calcular_raio()
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline, width=self.width, dash=(4, 2))

    #Desenha a figura final no canvas
    def desenhar_figura(self, canvas):
        raio = self.calcular_raio()
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline, width=self.width)