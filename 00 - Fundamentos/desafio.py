menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[5] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        print('Depósito')
        
        
        valor = float(input('Quanto será depositado: R$'))
        
        if valor > 0.00:
            saldo += valor #adiciona o valor do depósito ao saldo 
            extrato += f'Depósito realizado R${valor:.2f}\n' #mostra no extrato a operação realizada
            print('Valor depositado com sucesso!')

        else:
            print('Operação não realizada por erro no valor, Digite um valor válido.')

    
    elif opcao == '2':
        print('Sacar')

    
        valor = float(input('Quanto será sacado: R$')) 

        #Defindo operações que não podem ocorrer por incompatibilidade com a regra do sistema
        atingiu_limite_saldo = valor > saldo
        atingiu_limite_saque_por_vez = valor > limite
        atingiu_limite_saques = numero_saques >= LIMITE_SAQUES
        

        if atingiu_limite_saldo:
            print('Não possui limite suficiente para este saque.')

        elif atingiu_limite_saque_por_vez:
            print('Atingiu limite de valor por saque.')

        elif atingiu_limite_saques:
            print('Atingiu limite de saques por dia.')

        #Caso não ocorra nenhuma irregularidade
        elif valor > 0.00: #tem que ser maior que zero para que consiga sacar algo
                saldo -= valor #diminui do saldo o valor sacado
                extrato += f'Saque realizado R${valor:.2f}\n'
                numero_saques += 1 #adiciona um saque à variável "numero_saques"
                print('Valor sacado com sucesso!')
                
        
        else:
            print('Erro na operação. Valor incorreto.')
            
    
    elif opcao == '3':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == '5':
        print('Obrigado por usar nosso sistema.')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
