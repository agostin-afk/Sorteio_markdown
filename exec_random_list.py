import random
import re
import os
from pathlib import Path
from dotenv import load_dotenv
dotenv_path = Path(__file__).resolve().parent / 'dotenv_file' / '.env'
load_dotenv(dotenv_path, override=True)
class FileManager:
    def __init__(self,):
            self.mode_path = ""
    def open_path(self, path, mode_path="r"):
        try:
            file = open(path, mode_path, encoding="utf-8")
            return file
        except FileNotFoundError:
            print(f"Erro: O arquivo '{path}' não foi encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return None

    def close_path(self, file):
        try:
            file.close()
        except Exception as e:
            print(f"Erro ao fechar o arquivo: {e}")

class Filme(FileManager):
    def __init__(self):
        self.caminho = os.getenv('CAMINHO_MD', )
        self.filme = ""
        self.lista_filme = []
        self.ultimo_filme = ""
    def get_lista(self):
        """Lê a lista de filmes do arquivo e filtra apenas os não assistidos."""
        try:
            self.lista_filme = []  # Garante que a lista seja limpa antes de preencher
            file = self.open_path(self.caminho)
            linhas = file.readlines() #type: ignore
            for linha in linhas:
                if re.findall(r'\[ \]', linha):  # Filtra linhas com '[ ]'
                    self.lista_filme.append(linha.strip())
            self.close_path(file)
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
            file = self.open_path("filme_da_vez.txt", "w")
            file.write(self.filme) #type: ignore
            self.close_path(file)
        except Exception as e:
            return f"Erro ao salvar o filme: {str(e)}"

    def get_filme(self):
        """Lê o último filme salvo."""
        try:
            file = self.open_path("filme_da_vez.txt",)
            self.filme = file.read() #type: ignore
            self.close_path(file)
            return f"{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except FileNotFoundError:
            return "Nenhum filme salvo anteriormente."
        except Exception as e:
            return f"Erro ao obter o filme salvo: {str(e)}"

    def remove_filme(self):
        """Remove o filme atualmente salvo."""
        try:
            file = self.open_path("filme_da_vez.txt", "w")
            self.check()
            file.write("") #type: ignore
            self.close_path(file)
        except Exception as e:
            return f"Erro ao remover o filme: {str(e)}"
    def check(self):
        """Procura pelo filme e substitui '[ ]' por '[x]' na mesma linha."""
        try:
            file = self.open_path(self.caminho, "r+")
            conteudo = file.readlines() #type: ignore
            file.seek(0) #type: ignore
            encontrado = False
            for i, linha in enumerate(conteudo):
                # Verifica se a linha contém o filme e '[ ]'
                if re.search(re.escape(self.filme), linha) and '[ ]' in linha:
                    # Substitui '[ ]' por '[x]' na linha correspondente
                    conteudo[i] = re.sub(r'\[ \]', '[x]', linha)
                    encontrado = True
            
            if encontrado:
                # Sobrescreve o arquivo com o conteúdo atualizado
                file.writelines(conteudo) #type: ignore
                file.truncate()  #type: ignore
                # print(f"Filme atualizado: {self.filme}")
                self.close_path(file)
            else:
                print("O filme não foi encontrado ou já foi marcado como assistido.")
        except Exception as e:
            print(f"Erro ao atualizar o filme no arquivo: {str(e)}")
    def main(self):
        """Executa a lógica principal para verificar ou sortear um filme."""
        try:
            file = self.open_path("filme_da_vez.txt")
            if file.read().strip(): #type: ignore
                self.get_filme()
                return f"Assista o último filme da lista:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
            else:
                self.set_filme()
                self.close_path(file)
                return f"O filme da vez:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except FileNotFoundError:
            # Caso o arquivo não exista, gera um novo sorteio
            self.set_filme()
            return f"O filme da vez:\n{re.sub(r'^\d{1,3}\.\s\[ \]\s', '', self.filme)}"
        except Exception as e:
            return f"Erro ao processar o arquivo do filme: {str(e)}"