from controller import Controlador
from model.desenho import Desenho
from view import *

model = Desenho() #cria o objeto de Desenho
Interface = ViewInterface() #cria o objeto de Interface
Canvas = ViewCanvas() #cria o objeto de Canvas
controller = Controlador(model, Canvas, Interface) #controller precisa se comunicar/acessar model e view para CONTROLAR o que deve ser feito

#permite o view acessar os metodos de controller
Canvas.interface = Interface
Canvas.controller = controller
Interface.controller = controller

#permite o codigo se repetir
Interface.mainloop()