import json
import os


filmes = "cadastrofilme.json"

def dadosfilme():
    if os.path.exists(filmes):
        with open(filmes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
   
def obterdadosfilmes():

    nome = input("Digite o nome do filme:")
    classificacao = int(input("Digite a classificação do filme: "))
    genero = input("Digite o gênero do filme: ")
    descricao = input("Informe a descrição do filme: ")

    filme = {
        "nome": nome,
        "classificacao": classificacao,
        "genero": genero,
        "descricao": descricao
    } 

    return filme

def cadastrarfilmes(receberfilme):
    db_filmes = dadosfilme()
    db_filmes.append(receberfilme)

    with open(filmes, "w", encoding="utf-8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)

def mostrardadosfilmes(db_filmes):
    if db_filmes:
        for filme in db_filmes:
            print(f"""
                Nome do filme: {filme["nome"]}
                Classificação do filme: {filme["classificacao"]}
                Gênero do filme: {filme["genero"]}
                Descrição do filme: {filme["descricao"]}
            """)
    else:
        print("Não existe nenhum filme cadastrado!")
        
def inciarsistema():
    db_filmes = dadosfilme()
    while True:
        print("Sistema de cadastro de filme:")
        print("="*90)
        print ("Opção 1 => Mostrar lista de filmes cadastrados")
        print ("Opção 2 => Cadastrar filmes")
        print ("Opção 3 => Sair do sistema")
        print("="*90)

        opcao = input("Escolha uma das opções do Menu: ")
        if opcao == "1":
            mostrardadosfilmes(db_filmes)
        elif opcao == "2":
            cadastrarfilmes(obterdadosfilmes())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção inválida. Escolha uma das opções do menu.")
        
inciarsistema()