import random
import re
class Filme():
    def __init__(self):
        self.caminho = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
        self.filme = ""
        self.lista_filme = []
        self.ultimo_filme = str
    def get_lista(self):
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if re.findall(r'\[ \]', linha) == ['[ ]']:
                    self.lista_filme.append(linha.strip())
    def set_filme(self):
        if self.lista_filme:
            self.filme = random.choice(self.lista_filme)
        else:
            return "Nenhum filme encontrado na lista."
        return self.filme
    def save_filme(self, filme):
        with open("filme_da_vez.txt", "w+", encoding="utf-8") as file:
            file.write(self.filme)
    def get_filme(self):
        with open("filme_da_vez.txt", "r+", encoding="utf-8") as file:
            self.filme = file.read()
            return self.filme 
    def last_filme(self,):
        with open("filme_da_vez.txt", "r+", encoding="utf-8") as file:
            if bool(file.read()):
                self.get_filme()
                return f"Assista o ultmo filme da lista: \n{self.filme}"
                pass
            else:
                self.set_filme()
                self.get_lista()
                self.save_filme(self,)
                return f"O filme da vez:\n{self.filme}"

test = Filme()
test.last_filme()
resultado = test.last_filme()

print(resultado)