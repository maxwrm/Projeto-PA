from .figuras import Figuras

class Quadrado(Figuras):
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
        margem = max(3, self.width)
        fim_x, fim_y = self.calcular_ponto_final()
        min_x = min(self.ini_x, fim_x) - margem
        max_x = max(self.ini_x, fim_x) + margem
        min_y = min(self.ini_y, fim_y) - margem
        max_y = max(self.ini_y, fim_y) + margem
        return min_x <= px <= max_x and min_y <= py <= max_y
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy
    
