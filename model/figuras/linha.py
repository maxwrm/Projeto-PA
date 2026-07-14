from .figuras import Figuras
from model.geometria import Geometria

class Linha(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y)
    
    def contem(self, px, py):
        margem = 3 + round(self.width/3)
        return Geometria.distancia(self.ini_x, self.ini_y, self.fim_x, self.fim_y, px, py) <= margem

    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
 
