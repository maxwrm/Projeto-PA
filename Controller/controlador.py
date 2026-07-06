from Model.Figuras import *
from Model.desenho import Desenho
from View.interface import Interface

class Controlador:
    def __init__(self, model:Desenho, view:Interface):
        self.model = model
        self.view = view

        self.figura_nova = None
    
    def iniciar_figura(self, event):
        tipo = self.view.get_tipo_figura()
        classe = eval(tipo)
        self.figura_nova = classe(event, fill=self.view.get_cor_preenchimento(), outline=self.view.get_cor_borda(), width=self.view.get_espessura())
    
    def atualizar_figura(self, event):
        if self.figura_nova == None:
            return
        
        if isinstance(self.figura_nova, Rabisco):
            self.view.desenhar_figuras(self.model.get_figuras())
            self.figura_nova.atualizar_coordenadas(event)
            self.figura_nova.desenhar_figura_pontilhada(canvas=self.view.canvas)

        else: #qualquer outra figura sem ser Rabisco
            self.figura_nova.atualizar_coordenadas(event)

            self.view.desenhar_figuras(self.model.get_figuras())

            self.figura_nova.desenhar_figura_pontilhada(canvas=self.view.canvas)
    
    def finalizar_figura(self, event):
        if self.figura_nova == None:
            return
        if not self.figura_nova.incompleta():
            self.model.adicionar_figura(self.figura_nova)

            self.view.desenhar_figuras(self.model.get_figuras())

            self.figura_nova = None # Evita continuar desenhando o tipo anterior se a figura escolhida no menu não estiver implementada
    
    def limpar(self):
        self.model.limpar_figuras()
        self.view.limpar_canvas()
    
    def desfazer(self):
        self.model.remover_figura()
        
        self.view.desenhar_figuras(self.model.get_figuras())