from abc import ABC, abstractmethod

class Ferramenta(ABC):

    """
    Classe abstrata que representa uma ferramenta de desenho. 
    Cada ferramenta é responsável por criar e manipular uma figura específica no canvas. 
    """

    def __init__(self, controlador):
        self.controlador = controlador
        self._figura_nova = None

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

    #Obtem o pontilhado de cada figura
    def obter_dash(self, figura):
        if figura.selecionada:
            return (4, 2)
        return None