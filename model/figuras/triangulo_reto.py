from .figuras import Figuras
from model.geometria import Geometria

class Triangulo_Reto(Figuras):

    """
    Classe modelo da figura Triangulo Reto, responsável por servir como modelo do que seria um Triangulo Reto, 
    armazenar os dados e coordenadas do Triangulo Reto, bem como realizar cálculos geométricos sobre o mesmo.
    """
    
    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)

    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Calcula os vértices do triângulo retângulo
    def calcular_vertices(self):
        A = (self.ini_x, self.ini_y)
        B = (self.ini_x, self.fim_y)
        C = (self.fim_x, self.fim_y)
        return A, B, C

    #Verfica se o triangulo está incompleto
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y) or self.ini_x == self.fim_x or self.ini_y == self.fim_y

    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        A, B, C = self.calcular_vertices()
        return Geometria.ponto_no_triangulo(A, B, C, (px, py))
    
    #Mover a figura, alterando suas coordenadas    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx

        self.ini_y += dy
        self.fim_y += dy