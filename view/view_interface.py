from tkinter import *
from tkinter import ttk

class ViewInterface(Tk):
    def __init__(self):
        super().__init__()
        #Titulo e tamanho da janela
        self.title("Desenhando Figuras com tkinter")
        self.geometry("1400x1400")
        
        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.controller = None

        # Widgets arranjados com Layout grid dentro de frame
        paddings = {'padx': 5, 'pady': 5}

        # label - figuras
        label_tipo_figura = ttk.Label(self.frame, text='Figuras:')
        label_tipo_figura.grid(column=0, row=1, sticky=W, **paddings)

        # option menu - figuras
        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
        option_menu_tipo_figura = ttk.OptionMenu(self.frame, self.tipo_figura_var,'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo', 'Quadrado')
        option_menu_tipo_figura.grid(column=1, row=1, sticky=W, **paddings)
        
        #label - cor - preenchimento
        label_cor_preenchimento = ttk.Label(self.frame, text='Cores de preenchimento:')
        label_cor_preenchimento.grid(column=2, row=1, sticky=W, **paddings)

        # option menu - cor - preenchimento
        self.cor_preenchimento_var = StringVar(self) # Guarda a cor de preenchimento selecionada no option menu
        option_menu_cor_preenchimento = ttk.OptionMenu(self.frame, self.cor_preenchimento_var, 'black', None, 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu_cor_preenchimento.grid(column=3, row=1, sticky=W, **paddings)

        # label - cor - borda
        label_cor_borda = ttk.Label(self.frame, text='Cores de borda:')
        label_cor_borda.grid(column=4, row=1, sticky=W, **paddings)

        # option menu - cor - borda
        self.cor_borda_var = StringVar(self) # Guarda a cor de borda selecionada no option menu
        option_menu_cor_borda = ttk.OptionMenu(self.frame, self.cor_borda_var,'black', 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu_cor_borda.grid(column=5, row=1, sticky=W, **paddings)

        # label - espessura do traço
        label_espessura = ttk.Label(self.frame, text='Espessura do traço:')
        label_espessura.grid(column=6, row=1, sticky=W, **paddings)

        # label - espessura do traço
        self.espessura_var = StringVar(self) #Guarda o valor da espessira do traço selecionada no option menu
        option_menu_espessura = ttk.OptionMenu(self.frame, self.espessura_var, 1, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
        option_menu_espessura.grid(column=7, row=1, sticky=W, **paddings)

        # Botões - também só associa a metodos de Controlador
        
        #Botao de limpar o canvas, que remove todas as figuras do canvas e da lista de figuras
        botao_limpar = ttk.Button(self.frame, text='Limpar', command=self.controller.limpar())
        botao_limpar.grid(column=7, row=0, sticky=W, **paddings)

        #Botao de desfazer a ultima figura desenhada, que remove a ultima figura da lista de figuras e redesenha todas as figuras no canvas
        botao_desfazer = ttk.Button(self.frame, text='↩', command=self.controller.desfazer())
        botao_desfazer.grid(column=0, row=0, sticky=W, **paddings)

    def get_tipo_figura(self):
        return self.tipo_figura_var.get()

    def get_cor_preenchimento(self):
        return self.cor_preenchimento_var.get()

    def get_cor_borda(self):
        return self.cor_borda_var.get()
    
    def get_espessura(self):
        return self.espessura_var.get()

    def get_paddings(self):
        return self.paddings