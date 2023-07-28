import os
display = """
====== Qual das seguintes operação você gostaria de realizar? ======
[1] Depositar.
[2] Sacar.
[3] Visualizar Extrato.
[0] Sair.
====================================================================
"""

QUANTIDADE_DE_SAQUES_DIARIO = 3
LIMITE_DE_SAQUE = 500.00
saldo = 0.00
quantidade_de_saques_realizados = 0 
extrato = ""

while True:
    opcao = int(input(display))
    os.system('clear') or None
    if opcao == 1:
        valor = float(input("Informe o valor a ser depositado: "))
        if valor <= 0.00:
            print("Erro - O valor a ser depositado não pode ser negativo!")
        else:
            saldo += valor
            extrato += f"Deposito - R${valor:.2f}\n"
            print("Deposito realizado com sucesso!") 
    elif opcao == 2:
        if quantidade_de_saques_realizados >= QUANTIDADE_DE_SAQUES_DIARIO:
            print("Erro - Você atingiu a quantidade maxima de saques diários! Tente") 
        else:
            valor = float(input("Informe o valor a ser sacado: ")) 
            if(valor > saldo):
                print("Erro - Você não possui saldo suficiente")
            else:
                saldo -= valor
                quantidade_de_saques_realizados += 1
                extrato += f"Saque - R${valor:.2f}\n"
                print("Saque realizado com sucesso!")    
    elif opcao == 3:
        print("EXTRATO".center(19, "#"))
        print(extrato)
        print(f"Saldo em conta - R${saldo:.2f}")
        print("#".center(19, "#"))
    elif opcao == 0:
        break
    else:
        print("Opção Inválida! Tente novamente.")
    
        
    


