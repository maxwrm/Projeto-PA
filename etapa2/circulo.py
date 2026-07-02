from tkinter import *
from figuras import Figuras

class Circulo(Figuras):

    def desenhar_figura_pontilhada(self, canvas):
        raio = ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline, dash=(4, 2))

    def desenhar_figura(self, canvas):
        raio = ((self.fim_x - self.ini_x) ** 2 + (self.fim_y - self.ini_y) ** 2) ** 0.5
        canvas.create_oval(self.ini_x - raio, self.ini_y - raio, self.ini_x + raio, self.ini_y + raio, fill=self.fill, outline=self.outline)