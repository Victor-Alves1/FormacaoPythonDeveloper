import textwrap

def menu():
    menu = """\n
    ========= MENU =========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f"Foi realizado um deposito no valor de R${valor:.2f}\n"
    else:
        print("Digite um valor válido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, contador, limite_saques):
    
        excedeu_saque = valor > limite
        excedeu_limite = contador > limite_saques
        excedeu_saldo = valor > saldo
        if excedeu_saque:
            print(f"Você ultrapassou o limite máximo de um saque. Você pode sacar no máximo R$ {limite}")
        elif excedeu_limite:
            print(f"Você ultrapassou o limite máximo de saques em um único dia. Você pode sacar no máximo {limite_saques}vezes ao dia")
        elif excedeu_saldo:
            print(f"O valor solicitado para o saque ultrapassa o valor em sua conta. Seu saldo atual é {saldo} Consulte seu saldo para saber mais informações.")
        elif valor > 0:
            saldo -= valor
            contador += 1
            extrato += f"Foi realizado um saque no valor de R${valor:.2f}\n" 
        else:
            print("Valor invalido.")
        return saldo, extrato
    

def extrair(saldo, /, *, extrato):
    print("\n------ Extrato ------")
    print(f"\n{extrato}")
    print(f"Saldo: {saldo:.2f}")
    print("\n---------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF completo: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")

    nome =  input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print("===  Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf =input("Informe o CPF do usuário:")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("===  Conta criada com sucesso! ===")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuário não encontrado, fluxo de criação de conta errado!")

def listar_conta(contas):
    for conta in contas :
        linha = f"""\
        Agência : \t {conta['agencia']}
        C/C: \t {conta['numero_conta']}
        Titular: \t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_DE_SAQUES =  3
    AGENCIA = "0001"
    numero_saques = 0
    limite_por_saque = 500
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        operacao = menu()

        if operacao == "q" :
            print("Sessão encerrada!")
            break
        elif operacao == "s":
            valor = float(input("Digite o valor do saque : "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite_por_saque, 
                contador=numero_saques, 
                limite_saques=LIMITE_DE_SAQUES
            )
        elif operacao == "d":
            valor = float(input("Digite o valor do deposito : "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif operacao == "e":
            if extrato != "":
                extrair(saldo, extrato=extrato)
            else:
                print("Extrato vazio.")
        elif operacao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif operacao == "lc":
            listar_conta(contas)
        elif operacao == "nu":
            criar_usuario(usuarios)

        else:
            print("Operação invalida, digite uma operação válida. S para Saque, D para deposito, E para extrato e Q para sair da sessão.")

main()