from .controlador import Controlador
from tkinter import *
from view import *

class ControladorSelecao:

    def __init__(self, controller:Controlador):
        self.controller = controller
        self.desenho = controller.model_desenho
        self.view_interface = controller.view_interface

        root = self.view_interface

        root.bind("<Up>", self.atua_com(self.desenho.selecionada_para_topo))
        
        root.bind("<Down>", self.atua_com(self.desenho.selecionada_para_fundo))
        
        root.bind("<Left>", self.atua_com(self.desenho.selecionada_para_tras))
        
        root.bind("<Right>", self.atua_com(self.desenho.selecionada_para_frente))
        
        root.bind("<Control-c>", self.atua_com(self.desenho.copiar_selecionada))
        
        root.bind("<Control-v>", self.atua_com(self.desenho.colar))
        
        root.bind("<Delete>", self.atua_com(self.desenho.apaga_selecionada))

    def atualiza_cor_linha(self) :
        f = self.desenho.selecionada() 
        if f != None :
            f.cor_borda = self.view_interface.get_cor_borda() 
            self.controller.desenhar_todas_figuras()
        
    def atualiza_cor_preenchimento(self):
        f = self.desenho.selecionada() 
        if f != None:
            f.cor_preenchimento = self.view_interface.get_cor_preenchimento()
            self.controller.desenhar_todas_figuras()

    def atua_com(self, atua):
        def ignoraEvent(event):
            atua()
            self.controller.desenhar_todas_figuras()
        return ignoraEvent