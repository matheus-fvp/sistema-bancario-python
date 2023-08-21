import os
display = """
====== Qual das seguintes operação você gostaria de realizar? ======
[1] Depositar.
[2] Sacar.
[3] Visualizar Extrato.
[0] Sair.
====================================================================
"""

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Erro: O valor a ser depositado deve ser maior que 0.")
    else:
        saldo += valor
        extrato += f"Deposito - R${valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite_saque, quantidade_de_saques_realizados, limite_saques):
    if quantidade_de_saques_realizados >= limite_saques:
        print("Erro - Você atingiu a quantidade maxima de saques diários!") 
    else:
        valor = float(input("Informe o valor a ser sacado: ")) 
        if(valor > saldo):
            print("Erro - Você não possui saldo suficiente")
        elif valor >= limite_saque:
            print(f"Erro - O limite maximo por saque é de R${limite_saque:.2f}")
        else:
            saldo -= valor
            quantidade_de_saques_realizados += 1
            extrato += f"Saque - R${valor:.2f}\n"
            print("Saque realizado com sucesso!")
    return saldo, extrato, quantidade_de_saques_realizados
    
def verificarExtrato(saldo, /, *, extrato):
    if extrato == "":
        print("Não houve movimentações na conta.")
    else:
        print("EXTRATO".center(19, "#"))
        print(extrato)
        print(f"Saldo em conta - R${saldo:.2f}")
        print("#".center(19, "#"))

def main():
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
            saldo, extrato = depositar(saldo, valor, extrato)
                
        elif opcao == 2:
            saldo, extrato, quantidade_de_saques_realizados = sacar(saldo=saldo, valor=valor, extrato=extrato, limite_saque=LIMITE_DE_SAQUE, quantidade_de_saques_realizados=quantidade_de_saques_realizados, limite_saques=QUANTIDADE_DE_SAQUES_DIARIO)
                    
        elif opcao == 3:
            verificarExtrato(saldo, extrato=extrato)
        elif opcao == 0:
            break
        else:
            print("Opção Inválida! Tente novamente.")
            
main()


    


