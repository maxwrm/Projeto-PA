from .figuras import Figuras
from model.geometria import Geometria

class Triangulo_Reto(Figuras):
    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)

    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    def calcular_vertices(self):
        A = (self.ini_x, self.ini_y)
        B = (self.ini_x, self.fim_y)
        C = (self.fim_x, self.fim_y)
        return A, B, C

    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y) or self.ini_x == self.fim_x or self.ini_y == self.fim_y

    def contem(self, px, py):
        A, B, C = self.calcular_vertices()
        return Geometria.ponto_no_triangulo(A, B, C, (px, py))
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx

        self.ini_y += dy
        self.fim_y += dy