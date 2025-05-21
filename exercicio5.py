from exercicio4 import calcularmedia

alunos = []

def obterdadosaluno():
    nomealuno = input("Digite o nome completo do aluno: ")
    idadealuno = int(input("Informe a idade do aluno: "))
    emailaluno = input("Informe o email do aluno: ")
    seriealuno = int(input("Série do aluno: "))
    nota1aluno = int(input("Informe a primeira nota: "))
    nota2aluno = int(input("Informe a segunda nota: "))
    nota3aluno = int(input("Informe a terceira nota: "))

    return cadastraraluno(nomealuno, emailaluno, seriealuno, nota1aluno, nota2aluno, nota3aluno)

def cadastraraluno(nome,email,serie,nota1=0,nota2=0,nota3=0):

    notas = [nota1,nota2,nota3]

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "notas": notas,
            "media": calcularmedia(notas)
    }

    alunos.append(aluno)

    return alunos

def mostrardadoslunos(dadosalunos):
    for aluno in dadosalunos:
        print(f"Nome do aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]} | Série do aluno: {aluno["serie"]} | Notas do aluno: {aluno["notas"]} | Média do alunos: {aluno["media"]}")
    return

def iniciarsistema():
    while True:
        print("="*80)
        print ("Opção 1 => Mostrar lista de alunos cadastrados")
        print ("Opção 2 => Cadastrar aluno")
        print ("Opção 3 => Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == "1":
            mostrardadoslunos(alunos)
        elif opcao == "2":
            obterdadosaluno()
        else:
            print("Sistema finalizado.")
            break

iniciarsistema()