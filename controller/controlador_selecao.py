from .controlador import Controlador
from tkinter import *
from view import *

class ControladorSelecao:

    """
    Responsável por controlar os movimentos que podem serem executados 
    enquanto um objeto desenhado em tela (no canvas) é selecionado.
    """

    def __init__(self, controller:Controlador):
        self.controller = controller
        self.desenho = controller.model_desenho
        self.view_interface = controller.view_interface

        root = self.view_interface

        self.view_interface.botao_borda.config(command=self.escolher_e_atualizar_borda)
        self.view_interface.botao_preenchimento.config(command=self.escolher_e_atualizar_preenchimento)

        root.bind("<Up>", self.atua_com(self.desenho.selecionada_para_topo))
        
        root.bind("<Down>", self.atua_com(self.desenho.selecionada_para_fundo))
        
        root.bind("<Left>", self.atua_com(self.desenho.selecionada_para_tras))
        
        root.bind("<Right>", self.atua_com(self.desenho.selecionada_para_frente))
        
        root.bind("<Control-c>", self.atua_com(self.desenho.copiar_selecionada))
        
        root.bind("<Control-v>", self.atua_com(self.desenho.colar))
        
        root.bind("<Delete>", self.atua_com(self.desenho.apaga_selecionada))

        root.bind("<BackSpace>", self.atua_com(self.desenho.apaga_selecionada))

    #atualiza a borda da figura selecionada com a cor escolhida na interface
    def escolher_e_atualizar_borda(self):
        self.view_interface.escolher_cor_borda()
        self.atualiza_cor_borda()

    #atualiza o preenchimento da figura selecionada com a cor escolhida na interface
    def escolher_e_atualizar_preenchimento(self):
        self.view_interface.escolher_cor_preenchimento()
        self.atualiza_cor_preenchimento()

    #atualiza a borda da figura selecionada com a cor escolhida na interface
    def atualiza_cor_borda(self) :
        f = self.desenho.selecionada()
        if f != None :
            f.outline = self.view_interface.get_cor_borda() 
            self.controller.desenhar_todas_figuras()

    #atualiza o preenchimento da figura selecionada com a cor escolhida na interface        
    def atualiza_cor_preenchimento(self):
        f = self.desenho.selecionada() 
        if f != None:
            f.fill = self.view_interface.get_cor_preenchimento()
            self.controller.desenhar_todas_figuras()

    #atualiza a espessura da borda da figura selecionada com a espessura escolhida na interface
    def atualizar_espessura(self):
        f=  self.desenho.selecionada()
        if f != None:
            f.width = self.view_interface.get_espessura()
            self.controller.desenhar_todas_figuras()

    #função genérica para executar cada ação com o objeto selecionado
    def atua_com(self, atua):
        def ignoraEvent(event):
            atua()
            self.controller.desenhar_todas_figuras()
        return ignoraEvent
