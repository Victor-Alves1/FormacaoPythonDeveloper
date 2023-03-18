LIMITE_DE_SAQUES =  3
contador_saques = 0
limite_por_saque = 500
saldo = 0
extrato = ""

while True:
    operacao = input("""\n Bem vindo ao sistema bancário

    Gostaria de realizar qual das operações:
    Digite S para Saque;
    Digite D para depósito;
    Digite E para extrato;
    
    Ou Q para encerrar sua sessão.
    """)

    if operacao == "q" :
        print("Sessão encerrada!")
        break
    elif operacao == "s":
        valor_do_saque = float(input("Digite o valor do saque : "))
        excedeu_saque = valor_do_saque < limite_por_saque
        excedeu_limite = contador_saques < LIMITE_DE_SAQUES
        excedeu_saldo = valor_do_saque < saldo
        if excedeu_saque:
            print(f"Você ultrapassou o limite máximo de um saque. Você pode sacar no máximo R$ {limite_por_saque}")
        elif excedeu_limite:
            print(f"Você ultrapassou o limite máximo de saques em um único dia. Você pode sacar no máximo {LIMITE_DE_SAQUES}vezes ao dia")
        elif excedeu_saldo:
            print(f"O valor solicitado para o saque ultrapassa o valor em sua conta. Seu saldo atual é {saldo} Consulte seu saldo para saber mais informações.")
        elif valor_do_saque > 0:
            saldo -= valor_do_saque
            contador_saques += 1
            extrato += f"Foi realizado um saque no valor de R${valor_do_saque:.2f}\n"
        else:
            print("Saldo insuficiente.")
    elif operacao == "d":
        valor_do_deposito = float(input("Digite o valor do deposito : "))
        if valor_do_deposito > 0 :
            extrato += f"Foi realizado um deposito no valor de R${valor_do_deposito:.2f}\n"
        else:
            print("Digite um valor válido.")
    elif operacao == "e":
        if extrato != "":
            print("\n------ Extrato ------")
            print(f"\n{extrato}")
            print(f"Saldo: {saldo:.2f}")
            print("\n---------------------")
        else:
            print("Extrato vazio.")
    else:
        print("Operação invalida, digite uma operação válida. S para Saque, D para deposito, E para extrato e Q para sair da sessão.")