class Desenho:
    def __init__(self):
        self.figuras = []

    def adicionar_figura(self, figura):
        self.figuras.append(figura)
    
    def remover_figura(self):
        if self.figuras:
            self.figuras.pop()
    
    def get_figuras(self):
        """Retorna a lista de todas as figuras salvas"""
        return self.figuras
    
    def limpar_figuras(self):
        self.figuras.clear()