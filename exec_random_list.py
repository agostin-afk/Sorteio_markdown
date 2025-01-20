import random
import re

class Filme:
    def __init__(self):
        self.caminho = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\lista_filme_prog.md"
        self.filme = ""
        self.lista_filme = []
        self.ultimo_filme = ""

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
                self.check()
                file.write("")
        except Exception as e:
            return f"Erro ao remover o filme: {str(e)}"
    def check(self):
        """Procura pelo filme e substitui '[ ]' por '[x]' na mesma linha."""
        try:
            with open(self.caminho, 'r+', encoding='utf-8') as file:
                conteudo = file.readlines()  # Lê todas as linhas como uma lista
                file.seek(0)
                encontrado = False
                
                for i, linha in enumerate(conteudo):
                    # Verifica se a linha contém o filme e '[ ]'
                    if re.search(re.escape(self.filme), linha) and '[ ]' in linha:
                        # Substitui '[ ]' por '[x]' na linha correspondente
                        conteudo[i] = re.sub(r'\[ \]', '[x]', linha)
                        encontrado = True
                
                if encontrado:
                    # Sobrescreve o arquivo com o conteúdo atualizado
                    file.writelines(conteudo)
                    file.truncate()  # Garante que o arquivo seja truncado após a escrita
                    print(f"Filme atualizado: {self.filme}")
                else:
                    print("O filme não foi encontrado ou já foi marcado como assistido.")
        except Exception as e:
            print(f"Erro ao atualizar o filme no arquivo: {str(e)}")
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
