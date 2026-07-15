from .figuras import Figuras
from model.geometria import Geometria

class Borracha(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
        self.pontos = [(event.x, event.y)]
    
    #Atualiza as coordenadas do ponto final da borracha, adicionando o ponto à lista de pontos
    def atualizar_coordenadas(self, event):
        ponto = (event.x, event.y)
        self.pontos.append(ponto)
    
    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return False

    def contem(self, px, py):
        pass

    def mover(self, dx, dy):
        pass