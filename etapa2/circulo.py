from tkinter import *
from figuras import Figuras

class Circulo(Figuras):

    def desenhar_figura(self, canvas, pontilhado=False):
        raio = ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
        
        if pontilhado:
            canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline, dash=(4, 2))
        else:
            canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline)