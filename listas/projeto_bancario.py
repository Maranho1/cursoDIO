menu = """

[1] depositar
[2] sacar
[3] extrato
[0] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite a quantia que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Digite um valor válido!")

    elif opcao == '2':
        valor =  float(input("Digite a quantia que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_limite_saques = numero_de_saques > LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print(f"Limite de {limite} excedido.")

        elif excedeu_limite_saques:
            print("Limite de saques diarios excedido.")        

        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R${valor:.2f}\n"
            numero_de_saques += 1


    elif opcao == '3':
        print("\n==========EXTRATO=============")
        print(f"Não foram feitas transações." if not extrato else extrato)
        print(f"\nSALDO: {saldo:.2f}")
        print("================================")


    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Digite uma opção válida!")


#linkedin = Yago Maranho