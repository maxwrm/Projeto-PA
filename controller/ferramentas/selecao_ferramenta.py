from .ferramenta import Ferramenta

class Selecao_Ferramenta(Ferramenta) :

    """
    Classe responsável por controlar todos os movimento e dados, executados e obtidos, 
    sobre a seleção de cada objeto no canvas, enquanto o usuário interage com a interface e canvas.
    """

    ult_x = 0
    ult_y = 0

    #Seleciona uma figura
    def mouse_pressionado(self, event):
        self.ult_x = event.x
        self.ult_y = event.y
        self.controlador.model_desenho.limpa_selecao()
        self.controlador.model_desenho.seleciona(event.x, event.y)
        self.controlador.model_desenho.atualizar_figura_selecionada()
        self.controlador.desenhar_todas_figuras()

    #Faz movimentos com a figura selecionada
    def mouse_arrastado(self, event):
        figSel = self.controlador.model_desenho.selecionada()
        if figSel :         
            figSel.mover(event.x - self.ult_x, event.y - self.ult_y)
            self.ult_x = event.x
            self.ult_y = event.y
            self.controlador.desenhar_todas_figuras()

    def mouse_solto(self, event):
        pass

    def desenhar_figura(self, figura=None, dash=None):
        pass
