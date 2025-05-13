from exercicio4 import calcularmedia

def cadastraraluno(nome,email,serie,nota1,nota2,nota3):
    alunos = []

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

print (cadastraraluno("Miguel", "miguel@gmail.com", "2B", 10,8,9))