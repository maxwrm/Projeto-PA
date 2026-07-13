from tkinter import *
from model.figuras import *

class ViewCanvas:
    def __init__(self, interface):
        self.controller = None
        self.interface = interface

        # Área de desenho
        self.canvas = Canvas(self.interface.frame, bg=self.interface.get_cor_background(), width=1152, height=648)
        self.canvas.grid(column=0, row=2, columnspan=10, sticky=W, **self.interface.get_paddings())

        #Associa eventos à métodos da própria função, os quais apenas vão executar métodos definidos na classe Controlador e usador por controlador
        self.canvas.bind("<ButtonPress-1>", self.clique_mouse)
        self.canvas.bind("<B1-Motion>", self.arrastar_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

    #Limpa o canvas
    def limpar_canvas(self):
        self.canvas.delete('all')

    #Desenha as figuras, mas não decide qual delas será
    def desenhar_linha(self, ini_x, ini_y, fim_x, fim_y, fill, width, dash=None):
        self.canvas.create_line(ini_x, ini_y, fim_x, fim_y, fill=fill, width=width, dash=dash)

    def desenhar_retangulo(self, ini_x, ini_y, fim_x, fim_y, fill, outline, width, dash=None):
        self.canvas.create_rectangle(ini_x, ini_y, fim_x, fim_y, fill=fill, outline=outline, width=width, dash=dash)

    def desenhar_oval(self, ini_x, ini_y, fim_x, fim_y, fill, outline, width, dash=None):
        self.canvas.create_oval(ini_x, ini_y, fim_x, fim_y, fill=fill, outline=outline, width=width, dash=dash)

    def desenhar_rabisco(self, pontos, fill, width):
        self.canvas.create_line(pontos, fill=fill, width=width)

    
    def clique_mouse(self, event):
        self.controller.iniciar_figura(event)

    def arrastar_mouse(self, event):
        self.controller.atualizar_figura(event)

    def soltar_mouse(self, event):
        self.controller.finalizar_figura(event)