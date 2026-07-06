from tkinter import *
from .figuras import Figuras

class Quadrado(Figuras):
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
    def calcular_diagonal(self):
        return ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
    
    def calcular_lado(self):
        return max(abs(self.fim_x - self.ini_x), abs(self.fim_y - self.ini_y))

    def calcular_ponto_final(self):
        lado = self.calcular_lado()
        
        if self.fim_x >= self.ini_x:
            x = self.ini_x + lado
        else:
            x = self.ini_x - lado

        if self.fim_y >= self.ini_y:
            y = self.ini_y + lado
        else:
            y = self.ini_y - lado

        return x, y
    
    #Desenha a figura pontilhada no canvas
    def desenhar_figura_pontilhada(self, canvas):
        x, y = self.calcular_ponto_final()
        
        canvas.create_rectangle(self.ini_x, self.ini_y, x, y, fill=self.fill, outline=self.outline, width=self.width, dash=(4, 2))

    #Desenha a figura final no canvas
    def desenhar_figura(self, canvas):
        x, y = self.calcular_ponto_final()
        
        canvas.create_rectangle(self.ini_x, self.ini_y, x, y, fill=self.fill, outline=self.outline, width=self.width)
