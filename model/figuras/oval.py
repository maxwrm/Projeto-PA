from .figuras import Figuras

class Oval(Figuras):
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
        centro_x = (self.ini_x + self.fim_x) / 2
        centro_y = (self.ini_y + self.fim_y) / 2
        raio_x = abs(self.fim_x - self.ini_x) / 2
        raio_y = abs(self.fim_y - self.ini_y) / 2

        if raio_x == 0 or raio_y == 0:
            return False
        
        valor = ((px - centro_x)**2 / raio_x**2) + ((py - centro_y)**2 / raio_y**2)
        margem = 0.1
        return valor <= 1 + margem
    
    #Move a figura na tela
    def mover(self, dx, dy):
        self.ini_x += dx
        self.fim_x += dx
        self.ini_y += dy
        self.fim_y += dy