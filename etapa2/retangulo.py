from tkinter import *
from figuras import Figuras

class Retangulo(Figuras):
    def desenhar_figura(self, canvas, pontilhado=False):
        if pontilhado:
            canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline, dash=(4, 2))
        else:
            canvas.create_rectangle(self.ini_x, self.ini_y, self.fim_x, self.fim_y, fill=self.fill, outline=self.outline)