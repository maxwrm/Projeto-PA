from .figuras import Figuras
from model.geometria import Geometria

class Borracha():

    """
    Classe reponsável por definir borracha e atualizar suas coordenadas no canvas.
    """

    def __init__(self, event):
        self.x = event.x
        self.y = event.y

    #Atualiza as coordenadas da borracha
    def atualizar_coordenadas(self, event):
        self.x = event.x
        self.y = event.y