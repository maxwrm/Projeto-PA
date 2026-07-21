from .ferramenta import Ferramenta
from model.figuras import Selecao

class Selecao_Ferramenta(Ferramenta) :

    """
    Classe responsável por controlar todos os movimento e dados, executados e obtidos, 
    sobre a seleção de cada objeto no canvas, enquanto o usuário interage com a interface e canvas.
    """

    #Seleciona uma figura
    def mouse_pressionado(self, event):
        self._figura_nova = Selecao(event)
    
    #Faz movimentos com a figura selecionada
    def mouse_arrastado(self, event):
        if self._figura_nova is None:
            return

        self._figura_nova.atualizar_coordenadas(event)
        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self._figura_nova, dash=(4, 2))

        figsSel = self.controlador.model_desenho.selecionada()
        for seles in figsSel:         
            seles.mover(event.x - self._figura_nova.ult_x, event.y - self._figura_nova.ult_y)
            self.ult_x = event.x
            self.ult_y = event.y
            self.controlador.desenhar_todas_figuras()

    def mouse_solto(self, event):
        figSel = self.controlador.model_desenho.selecionada()
        if figSel :         
            figSel.mover(event.x - self.ult_x, event.y - self.ult_y)
            self.ult_x = event.x
            self.ult_y = event.y
            self.controlador.desenhar_todas_figuras()

    def desenhar_figura(self, figura=None, dash=None):
        pass
