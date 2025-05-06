def cadastraraluno(nome,email,serie,nota1,nota2,nota3):
    alunos = []

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "notas": [nota1,nota2,nota3]
    }


    alunos.append(aluno)

    return alunos

print (cadastraraluno("Miguel", "miguel@gmail.com", "2B", 10,8,9))