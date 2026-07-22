from .figuras import Figuras
from model.geometria import Geometria

class Circulo(Figuras):

    """
    Classe modelo da figura Circulo, responsável por servir como modelo do que seria um Circulo, 
    armazenar os dados e coordenadas do Circulo, bem como realizar cálculos geométricos sobre o mesmo.
    """

    def __init__(self, event, fill, outline, width=1):
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
    
    #Verifica se a figura está dentro da area do slecionar    
    def dentro(self, min_x, min_y, max_x, max_y):
        return min_x <= self.ini_x <= max_x and min_x <= self.fim_x <= max_x and min_y <= self.ini_y <= max_y and min_y <= self.fim_y <= max_y

    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        margem = ((px - self.ini_x)**2 + (py - self.ini_y)**2)**0.5
        return margem <= self.calcular_raio()
    
    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
 