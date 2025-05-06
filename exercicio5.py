def cadastraraluno(nome,email,serie):
    alunos = []

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie
    }

    alunos.append(aluno)

    return alunos

print (cadastraraluno("Miguel", "miguel@gmail.com", "2B"))