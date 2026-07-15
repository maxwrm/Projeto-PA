from .figuras import Figuras
from model.geometria import Geometria

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

    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        margem = ((px - self.ini_x)**2 + (py - self.ini_y)**2)**0.5
        return margem <= self.calcular_raio()
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
 