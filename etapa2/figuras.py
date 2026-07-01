from tkinter import *

class Figuras:
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
