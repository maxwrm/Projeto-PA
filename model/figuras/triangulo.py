from .figuras import Figuras

class Triangulo_Reto(Figuras):
    def __init__(self, event, fill="black", outline="black", width=1):
        super().__init__(event, fill, outline, width)
        pass

    def contem(self, px, py):
        pass
    
    def mover(self, dx, dy):
        pass