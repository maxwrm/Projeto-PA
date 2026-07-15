import copy

class Desenho:
    def __init__(self):
        self.figuras = []
        self.figuras_removidas = []  # Lista para armazenar figuras removidas para refazer
        self.indice_selecionada = -1
        self.buffer = None

    def adicionar_figura(self, figura):
        self.figuras.append(figura)
        self.figuras_removidas.clear()  # Limpa a lista de figuras removidas ao adicionar uma nova figura

    def remover_figura(self):
        if self.figuras:
            figura_removida = self.figuras.pop()
            self.figuras_removidas.append(figura_removida)
    
    def get_figuras(self):
        """Retorna a lista de todas as figuras salvas"""
        return self.figuras
    
    def get_figuras_removidas(self):
        """Retorna a lista de todas as figuras removidas"""
        return self.figuras_removidas
    
    def limpar_figuras(self):
        self.figuras.clear()
    
    def refazer_figura(self):
        """Refaz a última figura removida, se houver"""
        if self.figuras_removidas:
            self.figuras.append(self.figuras_removidas.pop())
    
    def limpa_selecao(self) :
        for figura in self.figuras:
            figura.selecionada = False
        self.indice_selecionada = -1

    def seleciona(self, px, py) :
        i = len(self.figuras)-1
        while i >= 0 and not self.figuras[i].contem(px, py) :
            i -= 1
        self.indice_selecionada = i

    def selecionada(self) :
        if self.indice_selecionada >= 0 :
            return self.figuras[self.indice_selecionada]
        else :
            return None
        
    #Para a figura selecionada ficar marcada com dash
    def atualizar_figura_selecionada(self):
        for figura in self.figuras:
            figura.selecionada = False

        if self.indice_selecionada != -1:
            self.figuras[self.indice_selecionada].selecionada = True
    
    # Copiar/Colar
    def copiar_selecionada(self) :
        self.buffer = copy.deepcopy(self.indice_selecionada())

    def colar(self) :
        if self.buffer != None :
            f = self.buffer
            f.mover(5, 5)
            self.figuras.append(f)
            self.buffer = copy.deepcopy(f)

    #**** Operações sobre a figura selecionada
    def selecionada_para_topo(self) :
        s = self.indice_selecionada 
        if s != -1 :
            f = self.figuras.pop(s)
            self.figuras.append(f)
            self.indice_selecionada = len(self.figuras)-1
        
    def selecionada_para_fundo(self) :
        s = self.indice_selecionada 
        if s != -1 :
            f = self.figuras.pop(s)
            self.figuras.insert(0, f)
            self.indice_selecionada = 0

    def selecionada_para_tras(self) :
        s = self.indice_selecionada 
        if s > 0 :
            self.figuras[s], self.figuras[s-1] = self.figuras[s-1], self.figuras[s]
            self.indice_selecionada -= 1

    def selecionada_para_frente(self) :
        s = self.indice_selecionada 
        if 0 <= s < len(self.figuras) - 1 :
            self.figuras[s], self.figuras[s+1] = self.figuras[s+1], self.figuras[s]
            self.selecionada += 1

    def apaga_selecionada(self) :
        s = self.indice_selecionada 
        if s != -1 :
            self.figuras.pop(s)
            self.indice_selecionada = -1
