from tkinter import *
from tkinter import ttk

class Canvas(Tk):
    def __init__(self):
        super().__init__()

        # Widgets arranjados com Layout grid dentro de frame
        self.paddings = {'padx': 5, 'pady': 5}

        self.tipo_figura_var = StringVar(self) # Guarda o tipo de figura selecionado no option menu
        self.cor_preenchimento_var = StringVar(self) # Guarda a cor de preenchimento selecionada no option menu
        self.cor_borda_var = StringVar(self) # Guarda a cor de borda selecionada no option menu
        
        #Titulo e tamanho da janela
        self.title("Desenhando Figuras com tkinter 2")
        self.geometry("1400x1400")
        
        #Frame principal da interface
        self.frame = ttk.Frame(self)
        self.frame.pack()

        # Área de desenho
        self.canvas = Canvas(self.frame, bg='white', width=1200, height=1200)
        self.canvas.grid(column=0, row=2, columnspan=10, sticky=W, **self.paddings)