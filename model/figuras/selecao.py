from .figuras import Figuras

class Selecao(Figuras):
    def __init__(self, event):
        super().__init__(event)
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
    
    #Atualiza as coordenadas do ponto final da seleção
    def atualizar_coordenadas(self, event):
        self.fim_x = event.x
        self.fim_y = event.y

    #Se os pontos iniciais e finais forem iguais, a seleção está incompleta
    def incompleta(self):
        return False

    def area(self):
        self.min_x = min(self.ini_x, self.fim_x)
        self.max_x = max(self.ini_x, self.fim_x) 
        self.min_y = min(self.ini_y, self.fim_y)
        self.max_y = max(self.ini_y, self.fim_y)
    
    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        pass

    #Verifica se a figura está dentro da area do slecionar    
    def dentro(self, min_x, min_y, max_x, max_y):
        pass

    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        pass