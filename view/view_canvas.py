from tkinter import *
from model.figuras import *

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

    #Limpa o canvas
    def limpar_canvas(self):
        self.canvas.delete('all')
    
    #Desenha todas as figuras no canvas
    def desenhar_figuras(self, figuras):
        self.limpar_canvas()
        for figura in figuras:
            self.desenhar_figura(figura)

    #Desenha a figura definitiva no canvas
    def desenhar_figura(self, figura):

        if isinstance(figura, Linha):
            self.canvas.create_line(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, width=figura.width)
        elif isinstance(figura, Retangulo):
            self.canvas.create_rectangle(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, outline=figura.outline, width=figura.width)
        elif isinstance(figura, Oval):
            self.canvas.create_oval(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, outline=figura.outline, width=figura.width)
        elif isinstance(figura, Quadrado):
            fim_x, fim_y = figura.calcular_ponto_final()
            self.canvas.create_rectangle(figura.ini_x, figura.ini_y, fim_x, fim_y, fill=figura.fill, outline=figura.outline, width=figura.width)
        elif isinstance(figura, Circulo):
            raio = figura.calcular_raio()
            self.canvas.create_oval(figura.ini_x - raio, figura.ini_y - raio, figura.ini_x + raio, figura.ini_y + raio, fill=figura.fill, outline=figura.outline, width=figura.width)
        elif isinstance(figura, Rabisco):
            self.canvas.create_line(figura.pontos, fill=figura.fill, width=figura.width)


    #Desenha a figura pontilhada no canvas
    def desenhar_figura_pontilhada(self, figura):

        if isinstance(figura, Linha):
            self.canvas.create_line(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, width=figura.width, dash=(4, 2))
        elif isinstance(figura, Retangulo):
            self.canvas.create_rectangle(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, outline=figura.outline, width=figura.width, dash=(4, 2))
        elif isinstance(figura, Oval):
            self.canvas.create_oval(figura.ini_x, figura.ini_y, figura.fim_x, figura.fim_y, fill=figura.fill, outline=figura.outline, width=figura.width, dash=(4, 2))
        elif isinstance(figura, Quadrado):
            fim_x, fim_y = figura.calcular_ponto_final()
            self.canvas.create_rectangle(figura.ini_x, figura.ini_y, fim_x, fim_y, fill=figura.fill, outline=figura.outline, width=figura.width, dash=(4,2))
        elif isinstance(figura, Circulo):
            raio = figura.calcular_raio()
            self.canvas.create_oval(figura.ini_x-raio, figura.ini_y-raio, figura.ini_x+raio, figura.ini_y+raio, fill=figura.fill, outline=figura.outline, width=figura.width, dash=(4, 2))
        elif isinstance(figura, Rabisco): #Teste do rabisco sem pontilhado
            self.canvas.create_line(figura.pontos, fill=figura.fill, width=figura.width)
        
    #Métodos que apenas chamam métodos da classe Controlador, para associar eventos do mouse a ações do controlador
    def clique_mouse(self, event):
        self.controller.iniciar_figura(event)

    def arrastar_mouse(self, event):
        self.controller.atualizar_figura(event)

    def soltar_mouse(self, event):
        self.controller.finalizar_figura(event)

