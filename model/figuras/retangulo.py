from .figuras import Figuras

class Retangulo(Figuras):

    """
    Classe modelo da figura Retângulo, responsável por servir como modelo do que seria um Retângulo, 
    armazenar os dados e coordenadas do Retângulo, bem como realizar cálculos geométricos sobre o mesmo.
    """

    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y) or self.ini_x == self.fim_x or self.ini_y == self.fim_y
    
    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        min_x = min(self.ini_x, self.fim_x)
        max_x = max(self.ini_x, self.fim_x) 
        min_y = min(self.ini_y, self.fim_y)
        max_y = max(self.ini_y, self.fim_y)
        return min_x <= px <= max_x and min_y <= py <= max_y

    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.fim_x += dx
        self.fim_y += dy