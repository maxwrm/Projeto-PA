from controller import Controlador
from model.desenho import Desenho
from view import *

model = Desenho() #cria o objeto de Desenho
interface = ViewInterface() #cria o objeto de Interface
canvas = ViewCanvas(interface) #cria o objeto de Canvas
controller = Controlador(model, canvas, interface) #controller precisa se comunicar/acessar model e view para CONTROLAR o que deve ser feito

#permite o view acessar os metodos de controller
canvas.controller = controller
interface.controller = controller

#permite o codigo se repetir
interface.mainloop()