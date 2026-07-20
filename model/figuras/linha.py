from .figuras import Figuras
from model.geometria import Geometria

class Linha(Figuras):

    """
    Classe modelo da figura Linha, responsável por servir como modelo do que seria uma Linha, 
    armazenar os dados e coordenadas da Linha, bem como realizar cálculos geométricos sobre a mesma.
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
    
    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        margem = 3 + round(self.width/3)
        return Geometria.distancia(self.ini_x, self.ini_y, self.fim_x, self.fim_y, px, py) <= margem

    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
 
