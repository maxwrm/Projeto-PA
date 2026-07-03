from tkinter import *
from abc import ABC, abstractmethod
class Figuras(ABC):
    @abstractmethod
    def desenhar_figura(self, canvas):
        pass

    #Atualiza as coordenadas do ponto final da figura
    @abstractmethod
    def atualizar_coordenadas(self, event):
        pass

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta
    @abstractmethod
    def esta_incompleta(self):
        pass
