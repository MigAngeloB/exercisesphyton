import json
import os

veiculos = "cadastroveiculos.json"

def dadosveiculo():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obterdadosveiculo():

    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite a modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))
    cor = input("Digite a cor do veículo: ")

    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cor": cor
    }

    return veiculo

def cadastrarveiculo(receberveiculo):
    db_veiuculos = dadosveiculo()
    db_veiuculos.append(receberveiculo)

    with open(veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiuculos, arq_json, indent=4, ensure_ascii=False)

def mostrardadosveiculos(db_veiuculos):
    if db_veiuculos:
        for veiculo in db_veiuculos:
            print(f"""
                Marca do carro: {veiculo["marca"]}
                Modelo do carro: {veiculo["modelo"]}
                Ano do carro: {veiculo["ano"]}
                Cor do carro: {veiculo["cor"]}
             """)
    else:
        print("Não existe nenhum carro cadastrado!")

def iniciarsistema():

    db_veiculos = dadosveiculo()
    while True:
        print("Sistema de cadastro de veículo:")
        print("="*90)
        print ("Opção 1 => Mostrar lista de veículos cadastrados")
        print ("Opção 2 => Cadastrar veículos")
        print ("Opção 3 => Sair do sistema")
        print("="*90)

        opcao = input("Escolha uma das opções do Menu: ")
        if opcao == "1":
            mostrardadosveiculos(db_veiculos)
        elif opcao == "2":
            cadastrarveiculo(obterdadosveiculo())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção inválida. Escolha uma das opções do menu.")
        
iniciarsistema()