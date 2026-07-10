class Desenho:
    def __init__(self):
        self.figuras = []
        self.figuras_removidas = []  # Lista para armazenar figuras removidas para refazer

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