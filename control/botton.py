from model import *
from view import *

class Bottons:
    #Quando o botão limpar é clicado, todas as figuras são removidas do canvas e da lista de figuras
    def limpar_canvas(self):
        self.canvas.delete("all")
        self.figuras = []

    def desfazer(self):
        if self.figuras != []:
            self.figuras.remove(self.figuras[-1])
            self.desenhar_figuras()
        else:
            pass