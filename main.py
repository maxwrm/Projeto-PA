from controller import Controlador, ControladorSelecao
from model.desenho import Desenho
from model.persistencia import Persistencia
from view import *

#model
model_desenho = Desenho() #cria o objeto de Desenho
model_persistencia = Persistencia()

#view
interface = ViewInterface() #cria o objeto de Interface
canvas = ViewCanvas(interface) #cria o objeto de Canvas
menu_arquivo = ViewMenuArquivo()

#control
controller = Controlador(model_desenho, model_persistencia, canvas, interface, menu_arquivo) #controller precisa se comunicar/acessar model e view para CONTROLAR o que deve ser feito
controlador_selecao = ControladorSelecao(controller)

#permite o view acessar os metodos de controller
canvas.controller = controller
interface.controller = controller
interface.menu_arquivo = menu_arquivo
menu_arquivo.controller = controller
interface.controller_selecao = controlador_selecao

#permite o codigo se repetir
interface.mainloop()