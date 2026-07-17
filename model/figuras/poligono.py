from .figuras import Figuras
from model.geometria import Geometria

class Poligono(Figuras):
    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)
        self.pontos = [(event.x, event.y)]
    
    def atualizar_coordenadas(self, event):
        if len(self.pontos) >= 2 and Geometria.tres_pontos_alinhados(self.pontos[-2], self.pontos[-1], (event.x, event.y)) :
            self.pontos[-1] = (event.x, event.y)
        else :
            self.pontos.append((event.x, event.y))

    def incompleta(self):
        return len(self.pontos) <= 2

    def contem(self, px, py):
        dentro = False
        n = len(self.pontos)
        
        # Se o polígono não tiver pelo menos 3 vértices, não é um polígono válido
        if n < 3:
            return False
            
        # Inicializa o último vértice do polígono como ponto de partida
        p1x, p1y = self.pontos[0]
        
        for i in range(n + 1):
            # Avança para o próximo vértice
            p2x, p2y = self.pontos[i % n]
            
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