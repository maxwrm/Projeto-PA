from model.figuras import *
from model.desenho import Desenho
from model.persistencia import Persistencia
from view import *
from .ferramentas import *

class Controlador:
    def __init__(self, model_desenho:Desenho, model_persistencia:Persistencia, view_canvas: ViewCanvas, view_interface: ViewInterface, view_menu_arquivo:ViewMenuArquivo):
        self.model_desenho = model_desenho
        self.model_persistencia = model_persistencia
        self.view_canvas = view_canvas
        self.view_interface = view_interface
        self.view_menu_arquivo = view_menu_arquivo

        #Dicionário que mapeia o nome da figura (usado na interface) para o seu respectivo estado/ferramenta.
        self.ferramentas = {
            "Linha": Linha_Ferramenta(self),
            "Retangulo": Retangulo_Ferramenta(self),
            "Oval": Oval_Ferramenta(self),
            "Quadrado": Quadrado_Ferramenta(self),
            "Circulo": Circulo_Ferramenta(self),
            "Rabisco": Rabisco_Ferramenta(self),
            "Borracha": Borracha_Ferramenta(self),
            "Poligono": Poligono_Ferramenta(self),
            "Triangulo_Reto": Triangulo_Reto_Ferramenta(self),
            "Selecao": Selecao_Ferramenta(self)
        }

        self.ferramenta_atual = None

    def iniciar_figura(self, event):
        tipo = self.view_interface.get_tipo_figura()
        self.ferramenta_atual = self.ferramentas.get(tipo)

        if self.ferramenta_atual is None: # Evita continuar caso a figura escolhida no menu não esteja implementada
            return
        
        self.mudar_ferramenta(self.ferramenta_atual)
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

    #<Double-Button-1>
    def mouse_clicado_2(self, event):
        # Como o <ButtonRelease-1> limpa a ferramenta_atual, precisamos resgatá-la
        tipo = self.view_interface.get_tipo_figura()
        ferramenta = self.ferramentas.get(tipo)

        if ferramenta == None:
            return
        
        # Verifica se a ferramenta possui a função doubleclick e a executa
        if hasattr(ferramenta, 'doubleclick'):
            ferramenta.doubleclick(event)
            
        self.ferramenta_atual = None

    #Redesenha, do zero, todas as figuras já salvas no model_desenho
    def desenhar_todas_figuras(self):
        self.view_canvas.limpar_canvas()
        for figura in self.model_desenho.get_figuras():
            ferramenta = self.ferramentas[type(figura).__name__]
            ferramenta.desenhar_figura(figura)

    def mudar_ferramenta(self, nova_ferramenta):
        self.model_desenho.limpa_selecao()
        self.ferramenta_atual = nova_ferramenta
        self.desenhar_todas_figuras()

    #Limpa todo o quadro canvas
    def limpar(self):
        self.model_desenho.limpar_figuras()
        self.view_canvas.limpar_canvas()

    def desfazer(self):
        self.model_desenho.remover_figura()
        self.desenhar_todas_figuras()

    def refazer(self):
        self.model_desenho.refazer_figura()
        self.desenhar_todas_figuras()

    def salvar(self, nome):
        """Salva o desenho atual"""
        figuras = self.model_desenho.get_figuras()
        self.model_persistencia.salvar(figuras, nome)
        arquivos = self.listar_arquivos()
        self.view_menu_arquivo.atualizar_arquivos_salvos(arquivos)
    
    def carregar(self, nome):
        """Carrega um desenho salvo"""
        figuras = self.model_persistencia.carregar(nome)
        self.model_desenho.limpar_figuras()
        for figura in figuras:
            self.model_desenho.adicionar_figura(figura)
        self.desenhar_todas_figuras()
    
    def listar_arquivos(self):
        """Retorna lista de arquivos salvos"""
        return self.model_persistencia.listar_salvos()
    
    def atualiza_lista(self):
        arquivos = self.listar_arquivos()
        self.view_menu_arquivo.atualizar_arquivos_salvos(arquivos)