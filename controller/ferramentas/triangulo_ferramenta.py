from .ferramenta import Ferramenta
from model.figuras import Triangulo_Reto

class Triangulo_Ferramenta(Ferramenta):

    def mouse_pressionado(self, event):
        self.figura_nova = Triangulo_Reto(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())
    
    def mouse_arrastado(self, event):
        pass
    
    def mouse_solto(self, event):
        pass
    
    def desenhar_figura(self, figura, dash=None):
        pass