from tkinter import *

class ViewCanvas:
    def __init__(self, interface):
        self.controller = None
        self.interface = interface

        # Área de desenho
        self.canvas = Canvas(self.interface.frame, bg='white', width=1200, height=1200)
        self.canvas.grid(column=0, row=2, columnspan=10, sticky=W, **self.interface.get_paddings())

        #Associa eventos à métodos da própria função, os quais apenas vão executar métodos definidos na classe Controlador e usador por controlador
        self.canvas.bind("<ButtonPress-1>", self.clique_mouse)
        self.canvas.bind("<B1-Motion>", self.arrastar_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.soltar_mouse)

    def limpar_canvas(self):
        self.canvas.delete('all')
    
    def desenhar_figuras(self, figuras):
        self.limpar_canvas()
        for figura in figuras:
            figura.desenhar_figura(canvas=self.canvas)

    def clique_mouse(self, event):
        self.controller.iniciar_figura(event)

    def arrastar_mouse(self, event):
        self.controller.atualizar_figura(event)

    def soltar_mouse(self, event):
        self.controller.finalizar_figura(event)