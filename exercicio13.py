import json
import os

agendamento = "cadastroagenda.json"

def dadosagendamento():
    if os.path.exists(agendamento):
        with open (agendamento, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
def obterdadosagendamento():

    nomecliente = input("Digite o nome do cliente: ")
    servico = input("Escolha o serviço desejado: Ex: Corte, Barba, Escova ou Hidratação: ")
    data = input("Escolha a data: (Siga o exemplo: 05/03/2025): ")
    hora = input("Escolha o horário: (Siga o exemplo: 15h30): ")
    obs = input("Observações (Opcional): ")

    agendamento = {
        "Nome": nomecliente,
        "Serviço": servico,
        "Data": data,
        "Hora": hora,
        "Obs.": obs
    }

    return agendamento

def cadastrarcliente(receberdados):
    db_agendamento = dadosagendamento()
    db_agendamento.append(receberdados)

    with open (agendamento, "w", encoding="utf-8") as arq_json:
        json.dump(db_agendamento, arq_json, indent=4, ensure_ascii=False)

def mostardadosagendamento(db_agendamento):
    if db_agendamento:
        for agendamento in db_agendamento:
            print(f"""
                Nome do cliente: {agendamento["Nome"]}
                Serviço: {agendamento["Serviço"]}
                Data: {agendamento["Data"]}
                Horário: {agendamento["Hora"]}
                Observações: {agendamento["Obs."]}
            """)
    else:
        print("Não existe nenhum cliente agendado!")

def iniciarsistema():

    db_agendamento = dadosagendamento
    while True:
        print("Sistema de agendamento:")
        print("="*90)
        print ("Opção 1 => Mostrar agenda completa")
        print ("Opção 2 => Fazer agendamento")
        print ("Opção 3 => Sair do sistema")
        print("="*90)

        opcao = input("Escolha uma das opções do Menu: ")
        if opcao == "1":
            mostardadosagendamento(db_agendamento)
        elif opcao == "2":
            cadastrarcliente(obterdadosagendamento())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção inválida. Escolha uma das opções do menu.")
        
iniciarsistema()