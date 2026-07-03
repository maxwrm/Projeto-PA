from tkinter import *
from abc import ABC, abstractmethod

class Figuras(ABC):
    #Desenha a figura pontilhada no canvas, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def desenhar_figura(self, canvas):
        pass

    #Atualiza as coordenadas do ponto final da figura, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def atualizar_coordenadas(self, event):
        pass

    #Se os pontos iniciais e finais forem iguais, a figura está incompleta, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def esta_incompleta(self):
        pass
