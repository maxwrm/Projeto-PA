from abc import ABC, abstractmethod

class Ferramenta(ABC):

    def __init__(self, controlador):
        self.controlador = controlador
        self.figura_nova = None

    #Cria a figura correspondente ao pressionar o mouse, abstractmethod, deve ser implementado nas classes filhas
    @abstractmethod
    def mouse_pressionado(self, event):
        pass

    #Atualiza a figura em construção e redesenha o canvas com a figura pontilhada
    @abstractmethod
    def mouse_arrastado(self, event):
        pass

    #Finaliza a figura em construção, adicionando-a ao modelo se estiver completa
    @abstractmethod
    def mouse_solto(self, event):
        pass

    #Aqui cada objeto sabe como sua figura correspondente deve ser desenhada
    @abstractmethod
    def desenhar_figura(self, figura, dash=None):
        pass
