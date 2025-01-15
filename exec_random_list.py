import json
import random
import re
import random
import re

def _get_filme():
    caminho = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
    lista_filmes = []
    
    # Abrir e processar o arquivo de filmes
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if re.findall(r'\[ \]', linha) == ['[ ]']:
                lista_filmes.append(linha.strip())  # Remove espaços extras e quebra de linha
    
    # Selecionar filme aleatório
    if lista_filmes:
        filme = random.choice(lista_filmes)
    else:
        return "Nenhum filme encontrado na lista."

    # Salvar o filme selecionado no arquivo "filme_da_vez.txt"
    with open("filme_da_vez.txt", "w", encoding="utf-8") as arquivo_filme:
        arquivo_filme.write(filme)
    
    # Chamar a função personalizada (caso exista) e retornar o resultado
    try:
        resultado = get_filme_da_vez(filme)  # Certifique-se de que essa função existe
        regex = re.sub(r'^[0-9]{1,3}[^\w\s]\s*', '', resultado).strip()
    except NameError:
        resultado = f"Filme da vez: {filme}"
    
    return f"{filme}"
def get_filme_da_vez(filme):
    print(filme)