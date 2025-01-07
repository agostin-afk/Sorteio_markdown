import json
import re
x = "C:\\Users\\agost\\OneDrive\\Documentos\\Obsidian Vault\\Filmes - insta_1.md"
with open(x, "r", encoding="utf-8") as line:
    string = line.readlines()
    string = string[:]
    for i in string:
        print(re.sub(r'^[0-9]{1,3}.', '',i)[:4], end="\n") if re.sub(r'^[0-9]{1,3}.', '',i)[:4] == " [x]" else print()
    # print(string)
    pass