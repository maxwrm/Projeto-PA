from tkinter import *
from figuras import Figuras

class Retangulo(Figuras):
    def desenhar_figura_pontilhada(self, canvas):
        canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline, dash=(4, 2))

    def desenhar_figura(self, canvas):
        canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline)