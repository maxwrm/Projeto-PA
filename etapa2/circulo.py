from tkinter import *
from figuras import Figuras

class Circulo(Figuras):
    def __init__(self, event, fill="black", outline="black"):
        self.ini_x = event.x
        self.ini_y = event.y
        self.fim_x = event.x
        self.fim_y = event.y
        self.fill = fill
        self.outline = outline
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def esta_incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y)

    def desenhar_figura_pontilhada(self, canvas):
        raio = ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline, dash=(4, 2))

    def desenhar_figura(self, canvas):
        raio = ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline)