import json
import os

filmes = "data.json"

def dadosfilme():
   if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
   
filmes = dadosfilme()

for filme in filmes
    print(filme[""])