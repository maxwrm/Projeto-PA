from .ferramenta import Ferramenta
from model.figuras import Linha

class Linha_Ferramenta(Ferramenta):

    """
    Classe responsável por controlar todos os movimento e dados, executados e obtidos, sobre a linha, 
    enquanto o usuário interage com a interface e canvas.
    """

    #Cria uma nova Linha a partir do ponto onde o mouse foi pressionado
    def mouse_pressionado(self, event):
        self._figura_nova = Linha(event, fill=self.controlador.view_interface.get_cor_borda(), outline=self.controlador.view_interface.get_cor_preenchimento(), width=self.controlador.view_interface.get_espessura())

    #Atualiza a figura em construção e redesenha o canvas com a figura pontilhada
    def mouse_arrastado(self, event):
        if self._figura_nova is None:
            return

        self._figura_nova.atualizar_coordenadas(event)
        self.controlador.desenhar_todas_figuras()
        self.desenhar_figura(self._figura_nova, dash=(4, 2))

    #Finaliza a figura em construção, adicionando-a ao modelo se estiver completa
    def mouse_solto(self, event):
        if self._figura_nova is not None and not self._figura_nova.incompleta():
            self.controlador.model_desenho.adicionar_figura(self._figura_nova)

        self.controlador.desenhar_todas_figuras()
        self._figura_nova = None
    
    #Desenha a linha no canvas
    def desenhar_figura(self, figura, dash=None):
        if dash==None:
            dash=self.obter_dash(figura)
        self.controlador.view_canvas.desenhar_linha(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, width=figura.width, dash=dash)
