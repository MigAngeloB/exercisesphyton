def cadastraraluno(nome,email,serie,nota,):
    alunos = []

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "nota": nota
    }

    alunos.append(aluno)

    return alunos

print (cadastraraluno("Miguel", "miguel@gmail.com", "2B", "10"))