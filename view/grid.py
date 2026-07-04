from tkinter import *
from tkinter import ttk
from view import Canvas

class Grid(Tk):
    def __init__(self):
        super().__init__()  
    
        # label - figuras
        self.label_figuras = ttk.Label(self.frame, text='Figuras:')
        self.label_figuras.grid(column=0, row=1, sticky=W, **self.paddings)

        # option menu - figuras
        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')
        option_menu.grid(column=1, row=1, sticky=W, **self.paddings)

        # label - cores - preenchimento
        self.label_preenchimento = ttk.Label(self.frame, text='Cores de preenchimento:')
        self.label_preenchimento.grid(column=2, row=1, sticky=W, **self.paddings)

        # option menu - cores - preenchimento
        self.cor_preenchimento_var = StringVar(self) # Guarda a cor de preenchimento selecionada no option menu
        option_menu = ttk.OptionMenu(self.frame, self.cor_preenchimento_var, 'black', None, 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu.grid(column=3, row=1, sticky=W, **self.paddings)

        # label - cores - borda
        self.label_borda = ttk.Label(self.frame, text='Cores de borda:')
        self.label_borda.grid(column=4, row=1, sticky=W, **self.paddings)

        # option menu - cores - borda
        self.cor_borda_var = StringVar(self) # Guarda a cor de borda selecionada no option menu
        option_menu = ttk.OptionMenu(self.frame, self.cor_borda_var,'black', 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu.grid(column=5, row=1, sticky=W, **self.paddings)

        self.lbl_fonte = ttk.Label(self.frame, text='Tamanho da fonte:')
        self.lbl_fonte.grid(column=6, row=1, sticky=W, **self.paddings)

        self.fonte_var = StringVar(self)
        option_menu_fonte = ttk.OptionMenu(self.frame, self.fonte_var, 1, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
        option_menu_fonte.grid(column=7, row=1, sticky=W, **self.paddings)

        #Botoes
        #Botao de limpar o canvas, que remove todas as figuras do canvas e da lista de figuras
        self.botao_limpar = ttk.Button(self.frame, text='Limpar', command=self.limpar_canvas)
        self.botao_limpar.grid(column=6, row=0, sticky=W, **self.paddings)

        #Botao de desfazer a ultima figura desenhada, que remove a ultima figura da lista de figuras e redesenha todas as figuras no canvas
        self.botao_desfazer = ttk.Button(self.frame, text='↩', command=self.desfazer)
        self.botao_desfazer.grid(column=0, row=0, sticky=W, **self.paddings)