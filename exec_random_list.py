import random
import re

class Filme:
    def __init__(self):
        self.caminho = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
        self.filme = ""
        self.lista_filme = []
        self.ultimo_filme = ""  # Corrigido para string vazia

    def get_lista(self):
        """Lê a lista de filmes do arquivo e filtra apenas os não assistidos."""
        try:
            self.lista_filme = []  # Garante que a lista seja limpa antes de preencher
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    if re.findall(r'\[ \]', linha):  # Filtra linhas com '[ ]'
                        self.lista_filme.append(linha.strip())
        except FileNotFoundError:
            return "Erro: O arquivo da lista de filmes não foi encontrado."
        except Exception as e:
            return f"Erro ao ler a lista de filmes: {str(e)}"

    def set_filme(self):
        """Seleciona um filme aleatório da lista."""
        self.get_lista()
        if self.lista_filme:
            self.filme = random.choice(self.lista_filme)
        else:
            return "Nenhum filme encontrado na lista."
        return self.filme

    def save_filme(self):
        """Salva o filme selecionado em um arquivo separado."""
        try:
            with open("filme_da_vez.txt", "w", encoding="utf-8") as file:
                file.write(self.filme)
        except Exception as e:
            return f"Erro ao salvar o filme: {str(e)}"

    def get_filme(self):
        """Lê o último filme salvo."""
        try:
            with open("filme_da_vez.txt", "r", encoding="utf-8") as file:
                self.filme = file.read()
                return f"{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except FileNotFoundError:
            return "Nenhum filme salvo anteriormente."
        except Exception as e:
            return f"Erro ao obter o filme salvo: {str(e)}"

    def remove_filme(self):
        """Remove o filme atualmente salvo."""
        try:
            with open("filme_da_vez.txt", "w", encoding="utf-8") as file:
                file.write("")  # Esvazia o conteúdo do arquivo
        except Exception as e:
            return f"Erro ao remover o filme: {str(e)}"

    def main(self):
        """Executa a lógica principal para verificar ou sortear um filme."""
        try:
            with open("filme_da_vez.txt", "r", encoding="utf-8") as file:
                if file.read().strip():  # Verifica se há algo no arquivo
                    self.get_filme()
                    return f"Assista o último filme da lista:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
                else:
                    self.set_filme()
                    return f"O filme da vez:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except FileNotFoundError:
            # Caso o arquivo não exista, gera um novo sorteio
            self.set_filme()
            return f"O filme da vez:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except Exception as e:
            return f"Erro ao processar o arquivo do filme: {str(e)}"


# Teste do código
test = Filme()
