from .ferramenta import Ferramenta
from model.figuras import Poligono

class Poligono_Ferramenta(Ferramenta):

    #Cria um novo Poligono a partir do ponto onde o mouse foi pressionado
    def mouse_pressionado(self, event):
        if self._figura_nova is None:
                # Cria o novo polígono apenas se não existir um em construção
                self._figura_nova = Poligono(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
        else:
            self._figura_nova.atualizar_coordenadas(event)

        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self._figura_nova, dash=(4, 2))

    def mouse_arrastado(self, event, dash=None, **kwargs):
        if self._figura_nova is None:
            return

        self.controlador.desenhar_todas_figuras()
        pontos_temporarios = self._figura_nova.pontos + [(event.x, event.y)]    
        self.controlador.view_canvas.desenhar_poligono(pontos_temporarios, fill=self._figura_nova.fill, outline=self._figura_nova.outline, width=self._figura_nova.width, dash=(4, 2))

    def mouse_solto(self, event):
        self.mouse_arrastado(event)

    def doubleclick(self, event, dash=None, **kwargs):
        if self._figura_nova is not None and not self._figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self._figura_nova)

        self._figura_nova = None
        self.controlador.desenhar_todas_figuras()

    def desenhar_figura(self, figura, dash=None, **kwargs):
        if dash==None:
            dash=self.obter_dash(figura)
        self.controlador.view_canvas.desenhar_poligono(figura.pontos, fill=figura.fill, width=figura.width, outline=figura.outline, dash=dash, **kwargs)