from .ferramenta import Ferramenta
from model.figuras import Poligono

class Poligono_Ferramenta(Ferramenta):
    figura_nova : Poligono = None

    def mouse_pressionado(self, event):
        self.controlador.desenhar_todas_figuras()
        if self.figura_nova == None :
            self.figura_nova = self.figura_nova = Poligono(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
        else :
            self.figura_nova.adiciona_ponto(event.x, event.y)
        if len(self.figura_nova.pontos) >= 1 :
            self.controlador.desenhar_todas_figuras()

    def mouse_arrastado(self, event, dash=None, **kwargs):
        if self.figura_nova != None :
            self.controlador.desenhar_todas_figuras()
            pts = self.figura_nova.pontos
            pts.append((event.x, event.y))
            if len(pts) >= 1 :
                self.controlador.view_canvas.desenhar_poligono(self.figura_nova.pontos, fill=self.figura_nova.fill, width=self.figura_nova.width, outline=self.figura_nova.outline, dash=dash, **kwargs)
            pts.pop()

    def mouse_solto(self, event):
        if self.figura_nova is not None and not self.figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self.figura_nova)

        self.controlador.desenhar_todas_figuras()
        self.figura_nova = None
    
    #<Double-Button-1>
    def mouse_clicado_2(self, event) :
        if not self.figura_nova.incompleta() :
            self.controlador.model_desenho.adicionar_figura.adiciona_figura(self.figura_nova)
            self.controlador.desenhar_todas_figuras()
        self.figura_nova = None        
        self.controlador.desenhar_todas_figuras()

    def desenhar_figura(self, figura, dash=None, **kwargs):
        if dash==None:
            dash=self.obter_dash(figura)
        self.controlador.view_canvas.desenhar_poligono(figura.pontos, fill=figura.fill, width=figura.width, outline=figura.outline, dash=dash, **kwargs)