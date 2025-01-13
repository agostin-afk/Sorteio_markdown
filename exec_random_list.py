import json
import random
import re
def _get_filme():
    x = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
    lista_filmes = []
    with open(x, "r", encoding="utf-8") as line:
        string = line.readlines()
        string = string[:]
        for i in string:
            # regex = re.sub(r'^[0-9]{1,3}.', '',i).strip()
            if re.findall(r'\[ \]', i) == ['[ ]']:
                lista_filmes.append(i[:-1])
            # print(regex)
        # print(string)
    return f"Filme da vez: {random.choice(lista_filmes)}"