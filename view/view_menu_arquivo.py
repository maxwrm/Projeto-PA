from tkinter import *
from tkinter import ttk


class ViewMenuArquivo(Tk):

    """
    Classe responsável por gerenciar o menu de arquivos da interface gráfica.
    """

    def __init__(self):
        super().__init__()
        self.controller = None
        self.ativo = False
        self.arquivo_salvo_nome = None
        self.arquivo_carregado = StringVar(master=self)
        self.arquivos_salvos = []

        # Configurações da janela
        self.title("Salvar/Carregar")
        self.geometry("400x400")
        self.resizable(False, False)
        self.withdraw()

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.paddings = {"padx": 5, "pady": 5}

        # Widgets do menu de arquivos:

        # Botão de salvar
        self.botaoSalvar = ttk.Button(self.frame, text="Salvar", command=self.botao_salvar)
        self.botaoSalvar.grid(column=0, row=0, **self.paddings)

        # Label para exibir o nome do arquivo salvo
        self.label_arquivo_nome = ttk.Label(self.frame, text="Nenhum arquivo")
        self.label_arquivo_nome.grid(column=1, row=0, **self.paddings)

        # Caixa de texto para digitar o nome do arquivo a ser salvo
        self.caixa_texto = ttk.Entry(self.frame, width=20)
        self.caixa_texto.grid(column=2, row=0, **self.paddings)
        self.caixa_texto.bind("<Return>", self.apertar_enter)

        # Botão de carregar
        self.botaoCarregar = ttk.Button(self.frame, text="Carregar", command=self.botao_carregar)
        self.botaoCarregar.grid(column=0, row=1, **self.paddings)

        # Combobox para selecionar o arquivo a ser carregado
        self.combobox_carregar = ttk.Combobox(self.frame, textvariable=self.arquivo_carregado, values=self.arquivos_salvos, state="readonly", width=20)
        self.combobox_carregar.grid(column=1, row=1, **self.paddings)
        self.combobox_carregar.set("salvamentos")

    #Ativa o menu, atualizando a lista de arquivos salvos e exibindo a janela
    def ativar(self):
        """Ativa o menu"""
        self.ativo = True
        if self.controller:
            arquivos = self.controller.listar_arquivos()
            self.atualizar_arquivos_salvos(arquivos)
        self.deiconify()

    #Desativa o menu, escondendo a janela
    def desativar(self):
        """Desativa o menu"""
        self.ativo = False
        self.withdraw()

    #Alterna entre ativar e desativar o menu
    def alternar_menu(self):
        """Alterna entre ativar e desativar o menu"""
        if self.ativo:
            self.desativar()
        else:
            self.ativar()

    #Método chamado quando o usuário pressiona Enter na caixa de texto, atualizando o nome do arquivo salvo e limpando a caixa de texto
    def apertar_enter(self, event):
        self.arquivo_salvo_nome = self.caixa_texto.get()
        self.label_arquivo_nome.config(text=self.arquivo_salvo_nome)
        self.caixa_texto.delete(0, END)

    #Atualiza a lista de arquivos salvos na combobox, mantendo o arquivo selecionado se ele ainda estiver na lista
    def atualizar_arquivos_salvos(self, lista):
        selecionado = self.combobox_carregar.get()
        self.arquivos_salvos = lista[:]
        self.combobox_carregar.config(values=self.arquivos_salvos)

        if selecionado in self.arquivos_salvos:
            self.combobox_carregar.set(selecionado)
        elif self.arquivos_salvos:
            self.combobox_carregar.set(self.arquivos_salvos[0])
        else:
            self.combobox_carregar.set("salvamentos")

    #Método chamado quando o usuário clica no botão de salvar, chamando o método correspondente no controller
    def botao_salvar(self):
        if self.arquivo_salvo_nome:
            self.controller.salvar(self.arquivo_salvo_nome)

    #Método chamado quando o usuário clica no botão de carregar, chamando o método correspondente no controller
    def botao_carregar(self):
        nome = self.combobox_carregar.get()
        if nome and nome != "salvamentos":
            self.controller.carregar(nome)

    def get_salvo_nome(self):
        return self.arquivo_salvo_nome

    def get_carregado_nome(self):
        return self.combobox_carregar.get()