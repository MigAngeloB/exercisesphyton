<<<<<<< HEAD
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
=======
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
>>>>>>> 7f3c6f90cc51861b48fe66fda4f2dd4d600cf250
    print (cliente["nome_completo"])