from .ferramenta import Ferramenta
from model.figuras import Triangulo_Reto

class Triangulo_Reto_Ferramenta(Ferramenta):

    """
    Classe responsável por controlar todos os movimento e dados, executados e obtidos, sobre o triangulo reto, 
    enquanto o usuário interage com a interface e canvas.
    """

    def mouse_pressionado(self, event):
        self._figura_nova = Triangulo_Reto(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
    
    def mouse_arrastado(self, event):
        if self._figura_nova is None:
            return

        self._figura_nova.atualizar_coordenadas(event)
        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self._figura_nova, dash=(4, 2))
    
    def mouse_solto(self, event):
        if self._figura_nova is not None and not self._figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self._figura_nova)

        self.controlador.desenhar_todas_figuras()
        self._figura_nova = None
    
    def desenhar_figura(self, figura, dash=None):
        if dash==None:
            dash=self.obter_dash(figura)
        A, B, C = figura.calcular_vertices()
        self.controlador.view_canvas.desenhar_triangulo(A, B, C, fill=figura.fill, width=figura.width, outline=figura.outline, dash=dash)