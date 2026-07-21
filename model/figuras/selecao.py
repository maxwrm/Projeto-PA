from .figuras import Figuras

class Selecao(Figuras):
    def __init__(self, event):
        super().__init__(event)
        self.ult_x = 0
        self.ult_y = 0

    #Atualiza as coordenadas do ponto final da seleção
    def atualizar_coordenadas(self, event):
        self.ult_x = event.x
        self.ult_y = event.y

    #Se os pontos iniciais e finais forem iguais, a seleção está incompleta
    def incompleta(self):
        return (self.ini_x, self.ini_y) == (self.fim_x, self.fim_y) or self.ini_x == self.fim_x or self.ini_y == self.fim_y
    
    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        pass

    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        pass