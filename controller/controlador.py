from model.figuras import *
from model.desenho import Desenho
from model.persistencia import Persistencia
from view import *
from .ferramentas import *

class Controlador:

    """
    Responsável por fazer o controle entre o'que é obtido do usuário na interface ou canvas, envidando esses dados ao model (modelo de cada figura), 
    e o'que é produzido de acordo com o dado obtido no model.
    """

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
    
    #iniciar a criação de uma figura, a partir do ponto onde o mouse foi pressionado 
    def iniciar_figura(self, event):
        tipo = self.view_interface.get_tipo_figura()
        self.ferramenta_atual = self.ferramentas.get(tipo)

        if self.ferramenta_atual is None: # Evita continuar caso a figura escolhida no menu não esteja implementada
            return
        
        self.selecionar_ferramenta(self.ferramenta_atual)
        self.ferramenta_atual.mouse_pressionado(event)

    #atualizar a figura em construção, enquanto o mouse é arrastado
    def atualizar_figura(self, event):
        if self.ferramenta_atual == None:
            return

        self.ferramenta_atual.mouse_arrastado(event)

    #finalizar a criação da figura, quando o mouse é solto
    def finalizar_figura(self, event):
        if self.ferramenta_atual == None:
            return

        self.ferramenta_atual.mouse_solto(event)
        self.ferramenta_atual = None

    #<Double-Button-1>, usado para finalizar a criação de figuras que necessitam de mais de 2 pontos, como o polígono
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

    #Muda a ferramenta atual para a nova ferramenta escolhida, limpando a seleção de figuras no model_desenho e redesenhando todas as figuras
    def selecionar_ferramenta(self, nova_ferramenta):
        self.model_desenho.limpa_selecao()
        self.ferramenta_atual = nova_ferramenta
        self.desenhar_todas_figuras()

    #Limpa todo o quadro canvas
    def limpar(self):
        self.model_desenho.limpar_figuras()
        self.view_canvas.limpar_canvas()

    #Desfaz a última figura realizada, removendo-a do model_desenho e redesenhando todas as figuras
    def desfazer(self):
        self.model_desenho.remover_figura()
        self.desenhar_todas_figuras()

    #Refaz a última figura desfeita, adicionando-a novamente ao model_desenho e redesenhando todas as figuras
    def refazer(self):
        self.model_desenho.refazer_figura()
        self.desenhar_todas_figuras()

    #Salva o desenho atual, chamando a função de salvar do model_persistencia e atualizando a lista de arquivos salvos na interface
    def salvar(self, nome):
        """Salva o desenho atual"""
        figuras = self.model_desenho.get_figuras()
        self.model_persistencia.salvar(figuras, nome)
        arquivos = self.listar_arquivos()
        self.view_menu_arquivo.atualizar_arquivos_salvos(arquivos)
    
    #Carrega um desenho salvo, chamando a função de carregar do model_persistencia, limpando o model_desenho e adicionando as figuras carregadas ao model_desenho, e redesenhando todas as figuras
    def carregar(self, nome):
        """Carrega um desenho salvo"""
        figuras = self.model_persistencia.carregar(nome)
        self.model_desenho.limpar_figuras()
        for figura in figuras:
            self.model_desenho.adicionar_figura(figura)
        self.desenhar_todas_figuras()
    
    #Retorna uma lista com os nomes dos arquivos salvos, chamando a função de listar_salvos do model_persistencia, similar ao get()
    def listar_arquivos(self):
        """Retorna lista de arquivos salvos"""
        return self.model_persistencia.listar_salvos()
    
    #Atualiza a lista de arquivos salvos na interface, chamando a função listar_arquivos() e atualizando a view_menu_arquivo com a lista obtida
    def atualiza_lista(self):
        arquivos = self.listar_arquivos()
        self.view_menu_arquivo.atualizar_arquivos_salvos(arquivos)
