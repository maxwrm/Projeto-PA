from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif tipo_figura_var.get() == 'rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda_var.get(), cor_preenchimento_var.get())
    elif tipo_figura_var.get() == 'retangulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif tipo_figura_var.get() == 'oval':
        figura_nova = ('oval', (event.x, event.y, event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif tipo_figura_var.get() == 'circulo':
        figura_nova = ('circulo', (event.x, event.y, event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif figura_nova[0] == "oval":
        figura_nova = ("oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    elif figura_nova[0] == "circulo":
        figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda_var.get(), cor_preenchimento_var.get())
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor_b, cor_p in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_p)
        elif fig == "rabisco":
            canvas.create_line(values, fill=cor_p)
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor_b, fill=cor_p)
        elif fig == 'oval':
            canvas.create_oval(values[0], values[1], values[2], values[3], outline=cor_b, fill=cor_p)
        elif fig == 'circulo':
            raio = ( (values[2] - values[0])**2 + (values[3] - values[1])**2 ) ** 0.5
            canvas.create_oval(values[0]-raio, values[1]-raio, values[0]+raio, values[1]+raio, outline=cor_b, fill=cor_p)   

def desenhar_figura_nova():
    fig, values, cor_b, cor_p = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2), fill=cor_borda_var.get())
    elif fig == "rabisco":
        canvas.create_line(values, dash=(4, 2), fill=cor_preenchimento_var.get())
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2), outline=cor_borda_var.get(), fill=cor_preenchimento_var.get())
    elif fig == "oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2), outline=cor_borda_var.get(), fill=cor_preenchimento_var.get())
    elif fig == 'circulo':
            raio = ( (values[2] - values[0])**2 + (values[3] - values[1])**2 ) ** 0.5
            canvas.create_oval(values[0]-raio, values[1]-raio, values[0]+raio, values[1]+raio, dash=(4, 2), outline=cor_borda_var.get(), fill=cor_preenchimento_var.get())  

def incompleta(figura):
    fig, values, cor_b, cor_p = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "oval":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "circulo":
        return (values[0], values[1]) == (values[2], values[3])


#***_MAIN_****#
figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
root.title("Desenhando Figuras com Tkinter")
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label - figuras
label = ttk.Label(frame, text='Figuras:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu - figuras
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,'linha', 'linha', 'rabisco', 'retangulo', 'oval', 'circulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# label - cores - preenchimento
label = ttk.Label(frame, text='Cores de preenchimento:')
label.grid(column=2, row=0, sticky=W, **paddings)

# option menu - cores - preenchimento
cor_preenchimento_var = StringVar(root) # Guarda a cor de preenchimento selecionada no option menu
option_menu = ttk.OptionMenu(frame, cor_preenchimento_var, 'black', None, 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
option_menu.grid(column=3, row=0, sticky=W, **paddings)

# label - cores - borda
label = ttk.Label(frame, text='Cores de borda:')
label.grid(column=4, row=0, sticky=W, **paddings)

# option menu - cores - borda
cor_borda_var = StringVar(root) # Guarda a cor de borda selecionada no option menu
option_menu = ttk.OptionMenu(frame, cor_borda_var,'black', 'black', 'white', 'red', 'blue', 'green', 'yellow', 'orange', 'purple')
option_menu.grid(column=5, row=0, sticky=W, **paddings)


# Área de desenho
canvas = Canvas(frame, bg='white', width=1200, height=1200)
canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()