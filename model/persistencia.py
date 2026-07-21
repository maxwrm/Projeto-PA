import pickle
import os

class Persistencia:

    """
    Classe responsável por gerenciar a persistência de dados, incluindo salvar, carregar e listar arquivos de figuras.
    """

    def __init__(self):
        self.pasta = "salvamentos"

        if not os.path.exists(self.pasta):
            os.makedirs(self.pasta)

    def get_caminho(self, nome:str):
        """monta e retorna o caminho para o arquivo """
        nome = nome.strip()
        if not nome.endswith(".pkl"):
            nome += ".pkl"
        return os.path.join(self.pasta, nome)
    
    #Salva a lista de figuras em um arquivo nomeado e retorna o nome do arquivo sem o sufixo
    def salvar(self, figuras, nome:str):
        """salva a lista de figuras em um arquivo nomeado e retorna o nome do arquivo sem o sufixo"""
        caminho = self.get_caminho(nome)
        with open(caminho, "wb") as arquivo:
            pickle.dump(figuras, arquivo)
        return nome.removesuffix(".pkl")

    #Carrega um arquivo salvo e retorna a lista de figuras correspondente
    def carregar(self, nome:str):
        """carrega um arquivo salvo e retorna a lista de figuras correspondente"""
        caminho = self.get_caminho(nome)
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    
    #Lista todos os arquivos de salvamento na pasta, retornando apenas os nomes sem o sufixo
    def listar_salvos(self):
        """retorna uma lista com o nome de todos os arquivos da pasta de salvamentos sem o sufixo"""
        arquivos = os.listdir(self.pasta)
        nomes = []
        for arquivo in arquivos:
            if arquivo.endswith(".pkl"):
                nomes.append(arquivo.removesuffix(".pkl"))
        return sorted(nomes)