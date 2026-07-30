from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

class ViewInterface(Tk):

    """
    Classe responsável por gerenciar a interface gráfica do usuário.
    lidando com a criação da janela principal, a configuração de widgets e a interação com o usuário.
    """

    def __init__(self):
        super().__init__()
        #Titulo e tamanho da janela
        self.title("Da Vinci")
        self.geometry("1400x1400")
        
        self.frame = ttk.Frame(self)
        self.frame.pack()

       
        self.controller = None
        self.menu_arquivo = None

        # Widgets arranjados com Layout grid dentro de frame
        self.paddings = {'padx': 5, 'pady': 5}

        #Cores padrões
        self._cor_background_hex = "#FFFFFF"
        self._cor_preenchimento_hex = "#000000"
        self._cor_borda_hex = "#000000"

        #Dicionário das figuras
        self._figuras_dicionario = {"/":"Linha", "○":"Circulo", "□":"Quadrado", "▭":"Retangulo", "⬭":"Oval", "◺": "Triangulo_Reto", "▨": "Poligono"}
        
        #frame das figuras
        self.frame_figuras = ttk.Frame(master=self.frame, borderwidth=5, relief="sunken", height=10)
        self.frame_figuras.grid(column=1, row=0, rowspan=2, sticky="ns", **self.paddings)

        #Guarda o tipo de figura selecionada
        self._tipo_figura_var = StringVar(value="Rabisco")

        #botoes das figuras
        col, ro = 0, 1
        for simbolo, nome_figura in self._figuras_dicionario.items():

            radiobutton_figura = Radiobutton(master=self.frame_figuras, text=simbolo, indicatoron=False, font=("", 15), variable=self._tipo_figura_var, value=nome_figura, height=1, width=2, relief="raised", borderwidth=3, command=self.ao_trocar_ferramenta)
            radiobutton_figura.grid(column=col, row=ro, padx=2, pady=2)
            if col > 0 and col % 4 == 0: 
                ro+=1
                col = -1
            col+=1

        # label - figuras
        label_tipo_figura = ttk.Label(self.frame_figuras, text='Formas', font=("", 8))
        label_tipo_figura.grid(column=0, row=0, sticky=N, columnspan=5, **self.paddings)
        
        #frame para cores
        self.frame_cores = ttk.Frame(master=self.frame, borderwidth=5, relief="sunken")
        self.frame_cores.grid(column=2, row=0, rowspan=2, sticky="ns", **self.paddings)

        #Botao para tirar o preenchimento 
        self.botao_sem_preenchimento = Button(master=self.frame_cores, text="Sem preenchimento", font=("", 8), command=self.get_sem_cor_preenchimento)
        self.botao_sem_preenchimento.grid(column=0, row=3, columnspan=2, sticky=S, **self.paddings)

        #Botão e indicador de preenchimento
        self.botao_preenchimento = ttk.Button(master=self.frame_cores, text='Cor Preenchimento/Linha', command=self.escolher_cor_preenchimento)
        self.botao_preenchimento.grid(column=0, row=1, sticky=W, **self.paddings)

        self.indicador_preenchimento = Label(master=self.frame_cores, width=3, height=1, bg=self._cor_preenchimento_hex)
        self.indicador_preenchimento.grid(column=1, row=1, sticky=W, **self.paddings)

        # Botão e Indicador de Borda
        self.botao_borda = ttk.Button(master=self.frame_cores, text='Cor Borda', command=self.escolher_cor_borda)
        self.botao_borda.grid(column=0, row=2, sticky=W, **self.paddings)
        
        self.indicador_borda = Label(master=self.frame_cores, width=3, height=1, bg=self._cor_borda_hex)
        self.indicador_borda.grid(column=1, row=2, sticky=W, **self.paddings)

        #Label de cores que fica abaixo dos botões de selecionar
        self.label_cores = Label(master=self.frame_cores, text="Cores", font=("", 8))
        self.label_cores.grid(column=0, row=0, columnspan=2, sticky=N)

        #frame de ferramentas
        self.frame_ferramentas = ttk.Frame(master=self.frame, borderwidth=5, relief="sunken")
        self.frame_ferramentas.grid(column=0, row=0, rowspan=2, sticky="ns", **self.paddings)

        #botão de pincel que ficará em ferramentas
        self.radiobutton_pincel = Radiobutton(master=self.frame_ferramentas, text="🖌", font=("", 15), value="Rabisco", variable=self._tipo_figura_var, height=1, width=2, relief="raised", borderwidth=3, indicatoron=False)
        self.radiobutton_pincel.grid(column=0, row=1, **self.paddings)

        #botão de borracha que ficará em ferramentas
        self.radiobutton_borracha = Radiobutton(master=self.frame_ferramentas, text="⌫", font=("", 15), value="Borracha", variable=self._tipo_figura_var, height=1, width=2, relief="raised", borderwidth=3, indicatoron=False)
        self.radiobutton_borracha.grid(column=1, row=1, **self.paddings)

        #botao de selecionar que ficará em ferramentas
        self.radiobutton_selecao = Radiobutton(master=self.frame_ferramentas, text="⇖", font=("", 15), value="Selecao", variable=self._tipo_figura_var, height=1, width=2, relief="raised", borderwidth=3, indicatoron=False)
        self.radiobutton_selecao.grid(column=0, row=2, **self.paddings)
        
        #variavel da espessura
        self._espessura_var = IntVar(value=3)

        #Escala de espessura do traço
        self.escala_espessura = Scale(master=self.frame_ferramentas, from_=1, to=50, orient="vertical", label="Pincel", variable=self._espessura_var)
        self.escala_espessura.grid(column=2, row=1, rowspan=2, sticky="ens", **self.paddings)

        #label de ferramentas
        self.label_ferramentas = Label(master=self.frame_ferramentas, text="Ferramentas", font=("", 8))
        self.label_ferramentas.grid(column=0, row=0, columnspan=3, sticky=S)
        
        #Botao de limpar o canvas, que remove todas as figuras do canvas e da lista de figuras
        botao_limpar = ttk.Button(self.frame, text='Limpar', command=self.botao_limpar)
        botao_limpar.grid(column=5, row=0, sticky=N, **self.paddings)

        #Botao de desfazer a ultima figura desenhada, que remove a ultima figura da lista de figuras e redesenha todas as figuras no canvas
        botao_desfazer = ttk.Button(self.frame, text='↩', command=self.botao_desfazer, width=3)
        botao_desfazer.grid(column=5, row=0, sticky=W, **self.paddings)

        #Botao de refazer a ultima figura removida, que adiciona a ultima figura removida de volta na lista de figuras e redesenha todas as figuras no canvas
        botao_refazer = ttk.Button(self.frame, text='↪', command=self.botao_refazer, width=3)
        botao_refazer.grid(column=5, row=0, sticky=E, **self.paddings)

        #Botao de alternar entre esconder ou mostar o menu_arquivo
        botao_alternar_menu = ttk.Button(self.frame, text="💾", command=self.botao_alternar_menu, width=3)
        botao_alternar_menu.grid(column=6,row=0, sticky=N, **self.paddings)

    #Escolhe a cor de preenchimento/linha, atualizando o indicador de cor e a variável correspondente
    def escolher_cor_preenchimento(self):
        if self._cor_preenchimento_hex == "":
            self._cor_preenchimento_hex = None
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento/linha", initialcolor=self._cor_preenchimento_hex)
        if cor[1]: # Se o usuário não cancelar a janela
            self._cor_preenchimento_hex = cor[1]
            self.indicador_preenchimento.config(bg=cor[1])

    #Escolhe a cor de borda, atualizando o indicador de cor e a variável correspondente
    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda", initialcolor=self._cor_borda_hex)
        if cor[1]:
            self._cor_borda_hex = cor[1]
            self.indicador_borda.config(bg=cor[1])


    def ao_trocar_ferramenta(self):
        if self.controller:
            # Usa o get() aqui para pegar o nome atual e buscar a ferramenta correspondente
            tipo = self.get_tipo_figura()
            ferramenta = self.controller.ferramentas.get(tipo)
            if ferramenta:
                self.controller.reset(ferramenta)

    def get_sem_cor_preenchimento(self):
        self._cor_preenchimento_hex = ""

    def get_cor_preenchimento(self):
        return self._cor_preenchimento_hex

    def get_cor_borda(self):
        return self._cor_borda_hex
    
    def get_tipo_figura(self):
        return self._tipo_figura_var.get()
    
    def get_espessura(self):
        return self._espessura_var.get()
    
    def get_cor_background(self):
        return self._cor_background_hex

    def get_paddings(self):
        return self.paddings

    #Métodos para os botões de limpar, desfazer, refazer e alternar menu, que chamam os métodos correspondentes no controller
    def botao_limpar(self):
        if self.controller:
            self.controller.limpar()

    def botao_desfazer(self):
        if self.controller:
            self.controller.desfazer()

    def botao_refazer(self):
        if self.controller:
            self.controller.refazer()
    
    def botao_alternar_menu(self):
        self.menu_arquivo.alternar_menu()