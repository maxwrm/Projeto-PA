from controller.controlador import Controlador
from model.desenho import Desenho
from model.persistencia import Persistencia
from view import *

model_desenho = Desenho() #cria o objeto de Desenho
model_persistencia = Persistencia()
interface = ViewInterface() #cria o objeto de Interface
canvas = ViewCanvas(interface) #cria o objeto de Canvas
menu_arquivo = ViewMenuArquivo()
controller = Controlador(model_desenho, model_persistencia, canvas, interface, menu_arquivo) #controller precisa se comunicar/acessar model e view para CONTROLAR o que deve ser feito


#permite o view acessar os metodos de controller
canvas.controller = controller
interface.controller = controller
interface.menu_arquivo = menu_arquivo
menu_arquivo.controller = controller

#permite o codigo se repetir
interface.mainloop()