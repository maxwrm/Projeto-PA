from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import ttk
from figuras import Figuras
from rabisco import Rabisco
from linha import Linha
from retangulo import Retangulo
from oval import Oval
from circulo import Circulo

class Interface(Tk):
    def __init__(self):
        super().__init__()
        
        #Lista que salva as figuras que já foram desenhadas no canvas 
        self.figuras = []
        self.figura_nova = None

        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu
        self.cor_preenchimento_var = StringVar(self) # Guarda a cor de preenchimento selecionada no option menu
        self.cor_borda_var = StringVar(self) # Guarda a cor de borda selecionada no option menu
        
        #Titulo e tamanho da janela
        self.title("Desenhando Figuras com tkinter 2")
        self.geometry("1400x1400")
        
        #Frame principal da interface
        self.frame = ttk.Frame(self)
        self.frame.pack()

        # Widgets arranjados com Layout grid dentro de frame
        paddings = {'padx': 5, 'pady': 5}

        # Área de desenho
        self.canvas = Canvas(self.frame, bg='white', width=1200, height=1200)
        self.canvas.grid(column=0, row=2, columnspan=10, sticky=W, **paddings)

        # label - figuras
        label = ttk.Label(self.frame, text='Figuras:')
        label.grid(column=0, row=1, sticky=W, **paddings)

        # option menu - figuras
        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')
        option_menu.grid(column=1, row=1, sticky=W, **paddings)

        # label - cores - preenchimento
        label = ttk.Label(self.frame, text='Cores de preenchimento:')
        label.grid(column=2, row=1, sticky=W, **paddings)

        # option menu - cores - preenchimento
        cor_preenchimento_var = StringVar(self) # Guarda a cor de preenchimento selecionada no option menu
        option_menu = ttk.OptionMenu(self.frame, self.cor_preenchimento_var, 'black', None, 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu.grid(column=3, row=1, sticky=W, **paddings)

        # label - cores - borda
        label = ttk.Label(self.frame, text='Cores de borda:')
        label.grid(column=4, row=1, sticky=W, **paddings)

        # option menu - cores - borda
        cor_borda_var = StringVar(self) # Guarda a cor de borda selecionada no option menu
        option_menu = ttk.OptionMenu(self.frame, self.cor_borda_var,'black', 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
        option_menu.grid(column=5, row=1, sticky=W, **paddings)

        #Botoes
        
        #Botao de limpar o canvas, que remove todas as figuras do canvas e da lista de figuras
        botao_limpar = ttk.Button(self.frame, text='Limpar', command=self.limpar_canvas)
        
        botao_limpar.grid(column=6, row=0, sticky=W, **paddings)
        #Botao de desfazer a ultima figura desenhada, que remove a ultima figura da lista de figuras e redesenha todas as figuras no canvas
        botao_desfazer = ttk.Button(self.frame, text='↩', command=self.desfazer)
        botao_desfazer.grid(column=0, row=0, sticky=W, **paddings)

        # Eventos de mouse associados ao canvas - com seus callbacks
        self.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    #Clica no botão do mouse para iniciar a criação de uma nova figura
    def iniciar_figura_nova(self, event):
        tipo = eval(self.tipo_figura_var.get())
        self.figura_nova = tipo(event, fill=self.cor_preenchimento_var.get(), outline=self.cor_borda_var.get())

    #Segura o botão do mouse para atualizar a figura nova, desenhando pontilhada enquanto o mouse se move
    def atualizar_figura_nova(self, event):
        if self.tipo_figura_var.get() == 'Rabisco':
            self.desenhar_figuras()
            self.figura_nova.atualizar_coordenadas(event, self.canvas)
        else:
            self.figura_nova.atualizar_coordenadas(event)
            self.desenhar_figuras()
            self.figura_nova.desenhar_figura_pontilhada(self.canvas)
        

    #Solta o botão do mouse para incluir a figura nova na lista de figuras e desenhar todas as figuras no canvas
    def incluir_figura_nova(self, event):
        if not self.figura_nova.esta_incompleta():
            self.figuras.append(self.figura_nova)
        self.desenhar_figuras()
        
    #Desenha todas as figuras no canvas, incluindo a figura nova se ela estiver sendo desenhada
    def desenhar_figuras(self):
        self.canvas.delete("all")
        for figura in self.figuras:
            figura.desenhar_figura(self.canvas)

    #Quando o botão limpar é clicado, todas as figuras são removidas do canvas e da lista de figuras
    def limpar_canvas(self):
        self.canvas.delete("all")
        self.figuras = []

    def desfazer(self):
        if self.figuras != []:
            self.figuras.remove(self.figuras[-1])
            self.desenhar_figuras()
        else:
            pass