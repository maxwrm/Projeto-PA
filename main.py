from Controller.controlador import Controlador
from Model.desenho import Desenho
from View.interface import Interface

model = Desenho() #cria o objeto de Desenho
view = Interface() #cria o objeto de Interface
controller = Controlador(model, view) #controller precisa se comunicar/acessar model e view para CONTROLAR o que deve ser feito

#permite o view acessar os metodos de controller
view.controller = controller

#permite o codigo se repetir
view.mainloop()