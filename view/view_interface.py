from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

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
        self.paddings = {'padx': 5, 'pady': 5}

        #Cores padrões
        self.cor_preenchimento_hex = "#000000"
        self.cor_borda_hex = "#000000"

        # label - figuras
        label_tipo_figura = ttk.Label(self.frame, text='Figuras:')
        label_tipo_figura.grid(column=0, row=1, sticky=W, **self.paddings)

        # option menu - figuras
        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
        option_menu_tipo_figura = ttk.OptionMenu(self.frame, self.tipo_figura_var,'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo', 'Quadrado')
        option_menu_tipo_figura.grid(column=1, row=1, sticky=W, **self.paddings)
        
        #frame para cores
        self.frame_cores = ttk.Frame(master=self.frame, borderwidth=5, relief="sunken")
        self.frame_cores.grid(column=2, row=0, rowspan=2, **self.paddings)

        #Botão e indicador de preenchimento
        self.botao_preenchimento = ttk.Button(master=self.frame_cores, text='Cor Preenchimento/Linha', command=self.escolher_cor_preenchimento)
        self.botao_preenchimento.grid(column=0, row=0, sticky=W, **self.paddings)

        self.indicador_preenchimento = Label(master=self.frame_cores, width=3, height=1, bg=self.cor_preenchimento_hex)
        self.indicador_preenchimento.grid(column=1, row=0, sticky=W, **self.paddings)

        # Botão e Indicador de Borda
        self.botao_borda = ttk.Button(master=self.frame_cores, text='Cor Borda', command=self.escolher_cor_borda)
        self.botao_borda.grid(column=0, row=1, sticky=W, **self.paddings)
        
        self.indicador_borda = Label(master=self.frame_cores, width=3, height=1, bg=self.cor_borda_hex)
        self.indicador_borda.grid(column=1, row=1, sticky=W, **self.paddings)

        #Label de cores que fica abaixo dos botões de selecionar
        self.label_cores = Label(master=self.frame_cores, text="Cores", font=("", 8))
        self.label_cores.grid(column=0, row=3, columnspan=2)

        # label - espessura do traço
        label_espessura = ttk.Label(self.frame, text='Espessura do traço:')
        label_espessura.grid(column=6, row=1, sticky=W, **self.paddings)

        # label - espessura do traço
        self.espessura_var = StringVar(self) #Guarda o valor da espessira do traço selecionada no option menu
        option_menu_espessura = ttk.OptionMenu(self.frame, self.espessura_var, 1, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
        option_menu_espessura.grid(column=7, row=1, sticky=W, **self.paddings)

        # Botões - também só associa a metodos de Controlador
        
        #Botao de limpar o canvas, que remove todas as figuras do canvas e da lista de figuras
        botao_limpar = ttk.Button(self.frame, text='Limpar', command=self.botao_limpar)
        botao_limpar.grid(column=8, row=0, sticky=W, **self.paddings)

        #Botao de desfazer a ultima figura desenhada, que remove a ultima figura da lista de figuras e redesenha todas as figuras no canvas
        botao_desfazer = ttk.Button(self.frame, text='↩', command=self.botao_desfazer)
        botao_desfazer.grid(column=0, row=0, sticky=W, **self.paddings)

    def escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento/linha", initialcolor=self.cor_preenchimento_hex)
        if cor[1]: # Se o usuário não cancelar a janela
            self.cor_preenchimento_hex = cor[1]
            self.indicador_preenchimento.config(bg=cor[1])

    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda", initialcolor=self.cor_borda_hex)
        if cor[1]:
            self.cor_borda_hex = cor[1]
            self.indicador_borda.config(bg=cor[1])

    def get_cor_preenchimento(self):
        return self.cor_preenchimento_hex

    def get_cor_borda(self):
        return self.cor_borda_hex
    
    def get_tipo_figura(self):
        return self.tipo_figura_var.get()
    
    def get_espessura(self):
        return int(self.espessura_var.get())

    def get_paddings(self):
        return self.paddings

    def botao_limpar(self):
        if self.controller:
            self.controller.limpar()

    def botao_desfazer(self):
        if self.controller:
            self.controller.desfazer()