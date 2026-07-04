from model import *
from view import *

class Desenhar:     
    #Clica no botão do mouse para iniciar a criação de uma nova figura
    def iniciar_figura_nova(self, event):
        tipo = eval(self.tipo_figura_var.get())
        self.figura_nova = tipo(event, fill=self.cor_preenchimento_var.get(), outline=self.cor_borda_var.get(), width=self.fonte_var.get())

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