from abc import ABC, abstractmethod

class Figuras(ABC):

    """
    Classe abstrata que representa um modelo das figuras. 
    Cada figura é responsável por se redefinir e manipular seus dados e calculos. 
    """

    def __init__(self, event, fill="black", outline="black", width=1):
        self.ini_x = event.x
        self.ini_y = event.y
        self.fim_x = event.x
        self.fim_y = event.y
        self.fill = fill
        self.width = width
        self.outline = outline
        self.selecionada = False
        self._figuras = []

    #Atualiza as coordenadas do ponto final da figura, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def atualizar_coordenadas(self, event):
        pass

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def incompleta(self):
        pass

    #Verifica se o ponto clicado na tela contém uma figura
    @abstractmethod
    def contem(self, px, py):
        pass

    #Move a figura clicada
    @abstractmethod
    def mover(self, dx, dy):
        pass
    