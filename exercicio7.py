dados = []

def obterdadosuser():
    nomeuser = input("Digite seu nome completo: ")
    cpfuser = int(input("Informe seu CPF: (Apenas números)"))
    rguser = int(input("Informe seu RG: (Apenas números)"))
    nascimentouser = input("Informe sua data de nascimento: ")
    enderecouser = input("Digte seu endereço: ")
    cidadeuser = input("Informe a cidade: ")
    estadouser = input("Informe o estado: (Apenas sigla Exemplo: RJ)")
    telfixouser = int(input("Informe seu telefone fixo: "))
    telcelularuser = int(input("Informe seu telefone celular: "))
    emailuser = input("Digite seu email: ")

    return cadastraruser (nomeuser, cpfuser, rguser, nascimentouser, enderecouser, cidadeuser, estadouser, telfixouser, telcelularuser, emailuser)

def cadastraruser(nome,cpf,rg,nascimento,endereco,cidade,estado,telefonefixo,telefonecelular,email):

    user = {
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "nascimento": nascimento,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "telefone fixo": telefonefixo,
            "telefone celular": telefonecelular,
            "email": email
    }

    dados.append(user)

    return dados

def mostrardadosuser(dadosusers):
    for user in dadosusers:
        print(f"Nome: {user["nome"]} | CPF: {user["cpf"]} | RG: {user["rg"]} | Nascimento: {user["nascimento"]} | Endereço: {user["endereco"]}| Cidade: {user["cidade"]}| Telefone fixo: {user["telefonefixor"]}| Telefone celular: {user["telefonecelular"]}| Endereço: {user["endereco"]}| Email: {user["email"]}")
    return

def iniciarsistema():
    while True:
        print("="*80)
        print ("Opção 1 => Mostrar lista de usuários cadastrados")
        print ("Opção 2 => Cadastrar usuário")
        print ("Opção 3 => Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == "1":
            mostrardadosuser(dados)
        elif opcao == "2":
            obterdadosuser()
        else:
            print("Sistema finalizado.")
            break

=======
dados = []

def obterdadosuser():
    nomeuser = input("Digite seu nome completo: ")
    cpfuser = int(input("Informe seu CPF: (Apenas números)"))
    rguser = int(input("Informe seu RG: (Apenas números)"))
    nascimentouser = input("Informe sua data de nascimento: ")
    enderecouser = input("Digte seu endereço: ")
    cidadeuser = input("Informe a cidade: ")
    estadouser = input("Informe o estado: (Apenas sigla Exemplo: RJ)")
    telfixouser = int(input("Informe seu telefone fixo: "))
    telcelularuser = int(input("Informe seu telefone celular: "))
    emailuser = input("Digite seu email: ")

    return cadastraruser (nomeuser, cpfuser, rguser, nascimentouser, enderecouser, cidadeuser, estadouser, telfixouser, telcelularuser, emailuser)

def cadastraruser(nome,cpf,rg,nascimento,endereco,cidade,estado,telefonefixo,telefonecelular,email):

    user = {
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "nascimento": nascimento,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "telefone fixo": telefonefixo,
            "telefone celular": telefonecelular,
            "email": email
    }

    dados.append(user)

    return dados

def mostrardadosuser(dadosusers):
    for user in dadosusers:
        print(f"Nome: {user["nome"]} | CPF: {user["cpf"]} | RG: {user["rg"]} | Nascimento: {user["nascimento"]} | Endereço: {user["endereco"]}| Cidade: {user["cidade"]}| Telefone fixo: {user["telefonefixor"]}| Telefone celular: {user["telefonecelular"]}| Endereço: {user["endereco"]}| Email: {user["email"]}")
    return

def iniciarsistema():
    while True:
        print("="*80)
        print ("Opção 1 => Mostrar lista de usuários cadastrados")
        print ("Opção 2 => Cadastrar usuário")
        print ("Opção 3 => Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == "1":
            mostrardadosuser(dados)
        elif opcao == "2":
            obterdadosuser()
        else:
            print("Sistema finalizado.")
            break
=======
dados = []

def obterdadosuser():
    nomeuser = input("Digite seu nome completo: ")
    cpfuser = int(input("Informe seu CPF: (Apenas números)"))
    rguser = int(input("Informe seu RG: (Apenas números)"))
    nascimentouser = input("Informe sua data de nascimento: ")
    enderecouser = input("Digte seu endereço: ")
    cidadeuser = input("Informe a cidade: ")
    estadouser = input("Informe o estado: (Apenas sigla Exemplo: RJ)")
    telfixouser = int(input("Informe seu telefone fixo: "))
    telcelularuser = int(input("Informe seu telefone celular: "))
    emailuser = input("Digite seu email: ")

    return cadastraruser (nomeuser, cpfuser, rguser, nascimentouser, enderecouser, cidadeuser, estadouser, telfixouser, telcelularuser, emailuser)

def cadastraruser(nome,cpf,rg,nascimento,endereco,cidade,estado,telefonefixo,telefonecelular,email):

    user = {
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "nascimento": nascimento,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "telefone fixo": telefonefixo,
            "telefone celular": telefonecelular,
            "email": email
    }

    dados.append(user)

    return dados

def mostrardadosuser(dadosusers):
    for user in dadosusers:
        print(f"Nome: {user["nome"]} | CPF: {user["cpf"]} | RG: {user["rg"]} | Nascimento: {user["nascimento"]} | Endereço: {user["endereco"]}| Cidade: {user["cidade"]}| Telefone fixo: {user["telefonefixor"]}| Telefone celular: {user["telefonecelular"]}| Endereço: {user["endereco"]}| Email: {user["email"]}")
    return

def iniciarsistema():
    while True:
        print("="*80)
        print ("Opção 1 => Mostrar lista de usuários cadastrados")
        print ("Opção 2 => Cadastrar usuário")
        print ("Opção 3 => Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == "1":
            mostrardadosuser(dados)
        elif opcao == "2":
            obterdadosuser()
        else:
            print("Sistema finalizado.")
            break
iniciarsistema()