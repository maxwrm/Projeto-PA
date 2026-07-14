from .ferramenta import Ferramenta

class Selecao_Ferramenta(Ferramenta) :
    ult_x = 0
    ult_y = 0

    def mouse_pressionado(self, event):
        self.ult_x = event.x
        self.ult_y = event.y
        self.controlador.model_desenho.limpa_selecao()
        self.controlador.model_desenho.seleciona(event.x, event.y)
        self.controlador.desenhar_todas_figuras()

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
