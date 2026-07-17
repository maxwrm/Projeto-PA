from .ferramenta import Ferramenta
from model.figuras import Poligono

class Poligono_Ferramenta(Ferramenta):
    _figura_nova : Poligono = None

    def mouse_pressionado(self, event):
        self.controlador.desenhar_todas_figuras()
        if self._figura_nova == None :
            self._figura_nova = self._figura_nova = Poligono(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
        else :
            self._figura_nova.atualizar_coordenadas(event)
            self.desenhar_figura(self._figura_nova, dash=(4, 2))
        if len(self._figura_nova.pontos) > 1:
            self.controlador.desenhar_todas_figuras()

    def mouse_arrastado(self, event, dash=None, **kwargs):
        if self._figura_nova != None :
            self.controlador.desenhar_todas_figuras()
            pts = self._figura_nova.pontos
            pts.append((event.x, event.y))
            if len(pts) > 1 :
                self.controlador.view_canvas.desenhar_poligono(self._figura_nova.pontos, fill=self._figura_nova.fill, width=self._figura_nova.width, outline=self._figura_nova.outline, dash=dash, **kwargs)
            pts.pop()

    def mouse_solto(self, event):
        self.mouse_arrastado(event)

    def doubleclick(self, event):
        if not self._figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self._figura_nova)
            self.controlador.desenhar_todas_figuras()
        self._figura_nova = None        
        self.controlador.desenhar_todas_figuras()
        self.controlador.view_canvas.desenhar_poligono(self._figura_nova.pontos, fill=self._figura_nova.fill, width=self._figura_nova.width, outline=self._figura_nova.outline, dash=dash, **kwargs)
        self._figura_nova = None

    def desenhar_figura(self, figura, dash=None, **kwargs):
        if dash==None:
            dash=self.obter_dash(figura)
        self.controlador.view_canvas.desenhar_poligono(figura.pontos, fill=figura.fill, width=figura.width, outline=figura.outline, dash=dash, **kwargs)