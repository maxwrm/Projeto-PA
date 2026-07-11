from tkinter import *
from tkinter import ttk

class ViewMenuArquivo(Tk):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.ativo = False
        self.arquivo_salvo_nome = None
        self.arquivo_carregado_nome = StringVar()
        self.arquivos_salvos = []

        self.title("Salvar/Carregar")
        self.geometry("400x400")
        self.resizable(False, False)
        self.withdraw()
        
        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.paddings = {'padx': 5, 'pady': 5}

        self.botao_salvar = ttk.Button(self.frame, text="Salvar", command=self.botao_salvar)
        self.botao_salvar.grid(column=0, row=0, **self.paddings)

        self.label_arquivo_nome = ttk.Label(self.frame, text="Nenhum arquivo")
        self.label_arquivo_nome.grid(column=1, row=0, **self.paddings)
        
        self.caixa_texto = ttk.Entry(self.frame, width=20)
        self.caixa_texto.grid(column=2, row=0, **self.paddings)
        self.caixa_texto.bind("<Return>", self.apertar_enter)

        self.botao_carregar = ttk.Button(self.frame, text="Carregar", command=self.botao_carregar)
        self.botao_carregar.grid(column=0, row=1, **self.paddings)

        self.option_menu_carregar = ttk.OptionMenu(self.frame, self.arquivo_carregado_nome, "salvamentos", *self.arquivos_salvos)
        self.option_menu_carregar.grid(column=1, row=1, **self.paddings)

    def ativar(self):
        """Ativa o menu"""
        self.ativo = True
        self.deiconify()  # Mostra a janela
    
    def desativar(self):
        """Desativa o menu"""
        self.ativo = False
        self.withdraw()  # Esconde a janela
    
    def alternar(self):
        if not self.ativo:
            self.ativar()
        else: #self.ativo
            self.desativar()

    def apertar_enter(self, event):
        self.arquivo_salvo_nome = self.caixa_texto.get()
        self.label_arquivo_nome.config(text=self.arquivo_salvo_nome)  # Atualiza o label
        self.caixa_texto.delete(0, END)
    
    def atualizar_arquivos_salvos(self, lista):
        self.arquivos_salvos = lista[:]
    
    def botao_salvar(self):
        pass

    def botao_carregar(self):
        pass