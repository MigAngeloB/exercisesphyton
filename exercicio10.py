import json
import os

data  = "funcionarios.json"
    
def carregardados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
funcionarios = carregardados()

for funcionario in funcionarios:
    print (f"Nome e sobrenome do funcionário: {funcionario["nome"]} {funcionario["sobrenome"]} \n Salário do funcionário: R${funcionario["salario"]}")