menu = '''

******** MENU ********

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Item> '''
# variaveis principais
saldo = 0
limite = 500
extrato = " "
numero_saques = 0 
numero_depositos = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("*** Deposito ***")
        deposito = int(input("Insira o valor de deposito: "))
        if deposito > 0:
            saldo += deposito
            numero_depositos +=1
            print("Depósito realizado.")
        else:
            print("Depósito não realizado. Valor inválido.")
        
      
    elif opcao == "s":
        print("*** Sacar ***")
        valor_do_saque = int(input("Insira o valor do saque: "))
        if valor_do_saque <= saldo and valor_do_saque <= limite:
            saldo -= valor_do_saque
            numero_saques += 1  # Incrementa a quantidade de saques realizados
            print("Saque realizado.")
            if numero_saques >=3:
               print("Limite diário de saque excedido.")
        else:
            print("Não foi possível realizar o saque.")
                        
                

    elif opcao == "e":
        print("*** Extrato ***")
        print(f"Número de saques: {numero_saques}")
        print(f"Número de depositos: {numero_depositos}")
        print(f"Seu saldo é: {saldo}")


    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    