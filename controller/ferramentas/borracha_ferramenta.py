from .ferramenta import Ferramenta
from model.figuras import Borracha

class Borracha_Ferramenta(Ferramenta):

    """
    Classe responsável por controlar todos os movimento e comandos executados com a borracha, 
    enquanto o usuário interage com a interface e canvas.
    """

    #Deleta a figura inteira com o click
    def mouse_pressionado(self, event):
        self._figura_nova = Borracha(event)
        self.controlador.model_desenho.limpa_selecao()
        self.controlador.model_desenho.verificar(event.x, event.y)
        self.controlador.model_desenho.apaga_borracha()
        self.controlador.desenhar_todas_figuras()

    #Deleta a figura inteira quando passa por cima dela
    def mouse_arrastado(self, event):
        self._figura_nova.atualizar_coordenadas(event)
        self.controlador.model_desenho.limpa_selecao()
        self.controlador.model_desenho.verificar(event.x, event.y)
        self.controlador.model_desenho.apaga_borracha()
        self.controlador.desenhar_todas_figuras()

    def mouse_solto(self, event):
        pass

    def desenhar_figura(self, figura, dash=None):
        pass