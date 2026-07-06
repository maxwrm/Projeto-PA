from model.figuras import *
from model.desenho import Desenho
from view import *

class Controlador:
    def __init__(self, model:Desenho, view_canvas: ViewCanvas, view_interface: ViewInterface):
        self.model = model
        self.view_canvas = view_canvas
        self.view_interface = view_interface

        self.figura_nova = None
    
    def iniciar_figura(self, event):
        tipo = self.view_interface.get_tipo_figura()
        classe = eval(tipo)
        self.figura_nova = classe(event, fill=self.view_interface.get_cor_preenchimento(), outline=self.view_interface.get_cor_borda(), width=self.view_interface.get_espessura())
    
    def atualizar_figura(self, event):
        if self.figura_nova == None:
            return
        
        self.figura_nova.atualizar_coordenadas(event)
        self.view_canvas.desenhar_figuras(self.model.get_figuras())
        self.view_canvas.desenhar_figura_pontilhada(self.figura_nova)
    
    def finalizar_figura(self, event):
        if self.figura_nova == None:
            return
        elif not self.figura_nova.incompleta():
            self.model.adicionar_figura(self.figura_nova)

            self.view_canvas.desenhar_figuras(self.model.get_figuras())

            self.figura_nova = None # Evita continuar desenhando o tipo anterior se a figura escolhida no menu não estiver implementada
        else: #Se a figura estiver incompleta, apenas atualiza o canvas com as figuras já existentes
            self.view_canvas.desenhar_figuras(self.model.get_figuras())
            self.figura_nova = None
    
    def limpar(self):
        self.model.limpar_figuras()
        self.view_canvas.limpar_canvas()

    def desfazer(self):
        self.model.remover_figura()
        
        self.view_canvas.desenhar_figuras(self.model.get_figuras())