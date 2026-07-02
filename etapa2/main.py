from tkinter import *
from tkinter import ttk
from figuras import Figuras
from rabisco import Rabisco
from linha import Linha

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
root.title("Desenhando Figuras com Tkinter 2")
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5}

# Área de desenho
canvas = Canvas(frame, bg='white', width=1200, height=1200)
canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

frame.pack()

# label - figuras
label = ttk.Label(frame, text='Figuras:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu - figuras
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

#clica
def iniciar_figura_nova(event):
    global figura_nova
    tipo = eval(tipo_figura_var.get())
    figura_nova = tipo(event)

#segura
def atualizar_figura_nova(event):
    if tipo_figura_var.get() == 'Rabisco':
        desenhar_figuras()
        figura_nova.atualizar_coordenadas(event, canvas)
    else:
        figura_nova.atualizar_coordenadas(event)
        desenhar_figuras()
        figura_nova.desenhar_figura(canvas)
    

#solta
def incluir_figura_nova(event):
    if not figura_nova.esta_incompleta():
        figuras.append(figura_nova)
    desenhar_figuras()
    
def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar_figura(canvas)

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.mainloop()