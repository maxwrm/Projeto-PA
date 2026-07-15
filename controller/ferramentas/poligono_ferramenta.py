from .ferramenta import Ferramenta
from model.figuras import Poligono

class Poligono_Ferramenta(Ferramenta):

    def mouse_pressionado(self, event):
        self.figura_nova = Poligono(event.x, event.y, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
    
    def mouse_arrastado(self, event):
        if self.figura_nova is None:
            return

        self.figura_nova.atualizar_coordenadas(event)
        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self.figura_nova, dash=(4, 2))

    def mouse_solto(self, event):
        if self.figura_nova is not None and not self.figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self.figura_nova)

        self.controlador.desenhar_todas_figuras()
        self.figura_nova = None

    def desenhar_figura(self, figura, dash=None):
        self.controlador.view_canvas.desenhar_poligono(figura.pontos, fill=figura.fill, width=figura.width, dash=dash)