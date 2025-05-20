import json
import os

data  = "data.json"

def carregardados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

clientes = carregardados()

for cliente in clientes:
    print (cliente["nome_completo"])