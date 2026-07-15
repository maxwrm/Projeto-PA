from .ferramenta import Ferramenta
from model.figuras import Linha

class Linha_Ferramenta(Ferramenta):

    #Cria uma nova Linha a partir do ponto onde o mouse foi pressionado
    def mouse_pressionado(self, event):
        self.figura_nova = Linha(event, fill=self.controlador.view_interface.get_cor_preenchimento(), outline=self.controlador.view_interface.get_cor_borda(), width=self.controlador.view_interface.get_espessura())

    #Atualiza a figura em construção e redesenha o canvas com a figura pontilhada
    def mouse_arrastado(self, event):
        if self.figura_nova is None:
            return

        self.figura_nova.atualizar_coordenadas(event)
        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self.figura_nova, dash=(4, 2))

    #Finaliza a figura em construção, adicionando-a ao modelo se estiver completa
    def mouse_solto(self, event):
        if self.figura_nova is not None and not self.figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self.figura_nova)

        self.controlador.desenhar_todas_figuras()
        self.figura_nova = None
    
    #Desenha a linha no canvas
    def desenhar_figura(self, figura, dash=None):
        if dash==None:
            dash=self.obter_dash(figura)
        self.controlador.view_canvas.desenhar_linha(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, width=figura.width, dash=dash)
