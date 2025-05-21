clientes = []

def obterdadoscliente():
    nome = input("Digite o nome do cliente: ")
    cpf = int(input("Informe o CPF do cliente: (Apenas números)"))
    rg = int(input("Informe o RG do cliente: (Apenas números)"))
    nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Digte o endereço do cliente: ")
    cidade = input("Informe a cidade do cliente: ")
    estado = input("Informe o estado do cliente: (Apenas sigla Exemplo: RJ)")
    telefone = int(input("Informe telefone fixo do cliente: "))
    celular = int(input("Informe o telefone celular do cliente: "))
    email = input("Digite seu email: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "nascimento": nascimento,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "celular": celular,
        "email": email
    }

    return cliente

def cadastrarcliente(dadoscliente):
    clientes.append(dadoscliente)

    return clientes

def mostrardadosclientes(dadosclientes):
    for cliente in dadosclientes:
        print(f"""
        Nome do cliente: {cliente["nome"]}
        CPF do cliente: {cliente["cpf"]}
        RG do cliente: {cliente["rg"]}
        Nascimento do cliente: {cliente["nascimento"]}
        Endereço do cliente: {cliente["endereco"]}
        Cidade do cliente: {cliente["cidade"]}
        Estado do cliente: {cliente["estado"]}
        Telefone do cliente: {cliente["telefone"]}
        Celular do cliente: {cliente["celular"]}
        Email do cliente: {cliente["email"]}
        """)

def inciarsistema():
    while True:
        print("")
        print("="*90)
        print ("Opção 1 => Mostrar lista de clientes")
        print ("Opção 2 => Cadastrar clientes")
        print ("Opção 3 => Sair do sistema")
        print("="*90)

        opcao = input("Escolha uma das opções do Menu: ")
        if opcao == "1":
            mostrardadosclientes(clientes)
        elif opcao == "2":
            cadastrarcliente(obterdadoscliente())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção inválida. Escolha uma das opções do menu.")

clientes = []

def obterdadoscliente():
    nome = input("Digite o nome do cliente: ")
    cpf = int(input("Informe o CPF do cliente: (Apenas números)"))
    rg = int(input("Informe o RG do cliente: (Apenas números)"))
    nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Digte o endereço do cliente: ")
    cidade = input("Informe a cidade do cliente: ")
    estado = input("Informe o estado do cliente: (Apenas sigla Exemplo: RJ)")
    telefone = int(input("Informe telefone fixo do cliente: "))
    celular = int(input("Informe o telefone celular do cliente: "))
    email = input("Digite seu email: ")

    cliente = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "nascimento": nascimento,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "celular": celular,
        "email": email
    }

    return cliente

def cadastrarcliente(dadoscliente):
    clientes.append(dadoscliente)

    return clientes

def mostrardadosclientes(dadosclientes):
    for cliente in dadosclientes:
        print(f"""
        Nome do cliente: {cliente["nome"]}
        CPF do cliente: {cliente["cpf"]}
        RG do cliente: {cliente["rg"]}
        Nascimento do cliente: {cliente["nascimento"]}
        Endereço do cliente: {cliente["endereco"]}
        Cidade do cliente: {cliente["cidade"]}
        Estado do cliente: {cliente["estado"]}
        Telefone do cliente: {cliente["telefone"]}
        Celular do cliente: {cliente["celular"]}
        Email do cliente: {cliente["email"]}
        """)

def inciarsistema():
    while True:
        print("")
        print("="*90)
        print ("Opção 1 => Mostrar lista de clientes")
        print ("Opção 2 => Cadastrar clientes")
        print ("Opção 3 => Sair do sistema")
        print("="*90)

        opcao = input("Escolha uma das opções do Menu: ")
        if opcao == "1":
            mostrardadosclientes(clientes)
        elif opcao == "2":
            cadastrarcliente(obterdadoscliente())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção inválida. Escolha uma das opções do menu.")

inciarsistema()