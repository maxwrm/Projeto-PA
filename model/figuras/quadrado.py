from .figuras import Figuras

class Quadrado(Figuras):

    """
    Classe modelo da figura Quadrado, responsável por servir como modelo do que seria um Quadrado, 
    armazenar os dados e coordenadas do Quadrado, bem como realizar cálculos geométricos sobre o mesmo.
    """

    def __init__(self, event, fill, outline, width=1):
        super().__init__(event, fill, outline, width)
    
    #Atualiza as coordenadas do ponto final da figura
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y)

    #Calcula a diagonal do quadrado
    def calcular_diagonal(self):
        return ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
    
    #Calcula do lado do quadrado
    def calcular_lado(self):
        return max(abs(self.fim_x - self.ini_x), abs(self.fim_y - self.ini_y))
    
    #Calcula a coordenada final do quadrado
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

    #Verifica se a figura está dentro da area do slecionar    
    def dentro(self, min_x, min_y, max_x, max_y):
        return min_x <= self.ini_x <= max_x and min_x <= self.fim_x <= max_x and min_y <= self.ini_y <= max_y and min_y <= self.fim_y <= max_y

    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        margem = max(3, self.width)
        fim_x, fim_y = self.calcular_ponto_final()
        min_x = min(self.ini_x, fim_x) - margem
        max_x = max(self.ini_x, fim_x) + margem
        min_y = min(self.ini_y, fim_y) - margem
        max_y = max(self.ini_y, fim_y) + margem
        return min_x <= px <= max_x and min_y <= py <= max_y
    
    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
    
