from model.figuras import *
from model.desenho import Desenho
from view import *
from .ferramentas import *

class Controlador:
    def __init__(self, model:Desenho, view_canvas: ViewCanvas, view_interface: ViewInterface):
        self.model = model
        self.view_canvas = view_canvas
        self.view_interface = view_interface

        #Dicionário que mapeia o nome da figura (usado na interface) para o seu respectivo estado/ferramenta.
        self.ferramentas = {
            "Linha": Linha_Ferramenta(self),
            "Retangulo": Retangulo_Ferramenta(self),
            "Oval": Oval_Ferramenta(self),
            "Quadrado": Quadrado_Ferramenta(self),
            "Circulo": Circulo_Ferramenta(self),
            "Rabisco": Rabisco_Ferramenta(self),
        }

        self.ferramenta_atual = None

    def iniciar_figura(self, event):
        tipo = self.view_interface.get_tipo_figura()
        self.ferramenta_atual = self.ferramentas.get(tipo)

        if self.ferramenta_atual is None: # Evita continuar caso a figura escolhida no menu não esteja implementada
            return

        self.ferramenta_atual.mouse_pressionado(event)

    def atualizar_figura(self, event):
        if self.ferramenta_atual == None:
            return

        self.ferramenta_atual.mouse_arrastado(event)

    def finalizar_figura(self, event):
        if self.ferramenta_atual == None:
            return

        self.ferramenta_atual.mouse_solto(event)
        self.ferramenta_atual = None

    #Redesenha, do zero, todas as figuras já salvas no model
    def desenhar_figuras(self):
        self.view_canvas.limpar_canvas()
        for figura in self.model.get_figuras():
            ferramenta = self.ferramentas[type(figura).__name__]
            ferramenta.desenhar_figura(figura)

    #Limpa todo o quadro canvas
    def limpar(self):
        self.model.limpar_figuras()
        self.view_canvas.limpar_canvas()

    def desfazer(self):
        self.model.remover_figura()
        self.desenhar_todas_figuras()

    def refazer(self):
        self.model.refazer_figura()
        self.desenhar_todas_figuras()
