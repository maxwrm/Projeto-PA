from tkinter import *
from tkinter import ttk


class ViewMenuArquivo(Tk):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.ativo = False
        self.arquivo_salvo_nome = None
        self.arquivo_carregado = StringVar(master=self)
        self.arquivos_salvos = []

        self.title("Salvar/Carregar")
        self.geometry("400x400")
        self.resizable(False, False)
        self.withdraw()

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.paddings = {"padx": 5, "pady": 5}

        self.botaoSalvar = ttk.Button(self.frame, text="Salvar", command=self.botao_salvar)
        self.botaoSalvar.grid(column=0, row=0, **self.paddings)

        self.label_arquivo_nome = ttk.Label(self.frame, text="Nenhum arquivo")
        self.label_arquivo_nome.grid(column=1, row=0, **self.paddings)

        self.caixa_texto = ttk.Entry(self.frame, width=20)
        self.caixa_texto.grid(column=2, row=0, **self.paddings)
        self.caixa_texto.bind("<Return>", self.apertar_enter)

        self.botaoCarregar = ttk.Button(self.frame, text="Carregar", command=self.botao_carregar)
        self.botaoCarregar.grid(column=0, row=1, **self.paddings)

        self.combobox_carregar = ttk.Combobox(self.frame, textvariable=self.arquivo_carregado, values=self.arquivos_salvos, state="readonly", width=20)
        self.combobox_carregar.grid(column=1, row=1, **self.paddings)
        self.combobox_carregar.set("salvamentos")

    def ativar(self):
        """Ativa o menu"""
        self.ativo = True
        if self.controller:
            arquivos = self.controller.listar_arquivos()
            self.atualizar_arquivos_salvos(arquivos)
        self.deiconify()

    def desativar(self):
        """Desativa o menu"""
        self.ativo = False
        self.withdraw()

    def alternar(self):
        if not self.ativo:
            self.ativar()
        else:
            self.desativar()

    def get_salvo_nome(self):
        return self.arquivo_salvo_nome

    def get_carregado_nome(self):
        return self.combobox_carregar.get()

    def apertar_enter(self, event):
        self.arquivo_salvo_nome = self.caixa_texto.get()
        self.label_arquivo_nome.config(text=self.arquivo_salvo_nome)
        self.caixa_texto.delete(0, END)

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

    def botao_salvar(self):
        if self.arquivo_salvo_nome:
            self.controller.salvar(self.arquivo_salvo_nome)

    def botao_carregar(self):
        nome = self.combobox_carregar.get()
        if nome and nome != "salvamentos":
            self.controller.carregar(nome)
