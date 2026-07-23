from .figuras import Figuras

class Selecao(Figuras):
    def __init__(self, event):
        super().__init__(event)
        self.fill = "#5B5B5B"
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
    
    #Verifica se o ponto clicado na tela contém a figura
    def contem(self, px, py):
        pass

    #Verifica se a figura está dentro da area do slecionar    
    def dentro(self, min_x, min_y, max_x, max_y):
        pass

    #Mover a figura, alterando suas coordenadas
    def mover(self, dx, dy):
        pass