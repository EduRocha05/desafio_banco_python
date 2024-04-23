menu = """

Escolha a opção desejada:

(D) Depositar
(S) Sacar
(E) Extrato
(X) Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("========== Deposito concluido ==========")

        else:
            print("Valor informado Invalido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("SALDO INSUFICIENTE")

        elif excedeu_limite:
            print("Operação falhou!! Valor do saque maior que o limite disponivel!")

        elif excedeu_saques:
            print("Operação falhou!! Numero de saques maior que o disponivel!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print("========== Deposito concluido ==========")

        else:
            print("Valor informado Invalido!")

    elif opcao == "e":
        print("\n >>>>>>>>>> Extrato <<<<<<<<<<")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

    elif opcao == "x":
        print("Sair")
        break

    else:
        print("Opção invalida, por favor selecione novamente!")
