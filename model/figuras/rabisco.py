from .figuras import Figuras
from model.geometria import Geometria

class Rabisco(Figuras):
    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)
        self.pontos = [(event.x, event.y)]
    
    #Atualiza as coordenadas do ponto final da figura, adicionando o ponto à lista de pontos
    def atualizar_coordenadas(self, event):
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
    
    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return len(self.pontos) <= 1

    # (px, py) está perto (<=epsilon) de self
    def contem(self, px, py):
        epsilon = 3
        return any(Geometria.distancia(x1, y1, x2, y2, px, py) <= epsilon
                    for (x1, y1), (x2, y2) in zip(self.pontos, self.pontos[1:]))
    
    def mover(self, dx, dy):
        for i in range(len(self.pontos)) :
            (x, y) = self.pontos[i]
            self.pontos[i] = (x+dx, y+dy)

