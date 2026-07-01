from tkinter import *
from tkinter import ttk
from figuras import Figuras
from rabisco import Rabisco

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
option_menu = ttk.OptionMenu(frame, tipo_figura_var,'linha', 'linha', 'rabisco', 'retangulo', 'oval', 'circulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

def criar_rabisco(event):
    global figura_nova
    figura_nova = Rabisco(event, canvas)
    figuras.append(figura_nova)


def adicionar_ponto_rabisco(event):
    if figura_nova is not None:
        figura_nova.adicionar_ponto(event)


# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', criar_rabisco)
canvas.bind('<B1-Motion>', adicionar_ponto_rabisco)
#canvas.bind('<ButtonRelease-1>', incluir_figura_nova)
root.mainloop()