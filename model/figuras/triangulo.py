from .figuras import Figuras
from model.geometria import Geometria

class Triangulo_Reto(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
        self.pontos = [(event.x, event.y)]

    def atualizar_coordenadas(self, event):
        if len(self.pontos) >= 2 and Geometria.tres_pontos_alinhados(self.pontos[-2], self.pontos[-1], (event.x, event.y)) :
                self.pontos[-1] = (event.x, event.y)
        else :
            self.pontos.append((event.x, event.y))

    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y) or self.ini_x == self.fim_x or self.ini_y == self.fim_y

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

    def contem(self, px, py):
        dentro = False
            
        # Inicializa o último vértice do polígono como ponto de partida
        p1x, p1y = self.pontos[0]
        
        for i in range(0, 3):
            # Avança para o próximo vértice
            p2x, p2y = self.pontos[i % 3]
            
            # Verifica se o raio horizontal intercepta a aresta do polígono
            if py > min(p1y, p2y):
                if py <= max(p1y, p2y):
                    if px <= max(p1x, p2x):
                        # Calcula a interceptação X exata da aresta
                        if p1y != p2y:
                            x_interceptado = (py - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        # Se o ponto estiver à esquerda da interceptação, inverte o estado
                        if p1x == p2x or px <= x_interceptado:
                            dentro = not dentro
                            
            p1x, p1y = p2x, p2y
            
        return dentro
    
    def mover(self, dx, dy):
        for i in range(len(self.pontos)) :
            (x, y) = self.pontos[i]
            self.pontos[i] = (x+dx, y+dy)