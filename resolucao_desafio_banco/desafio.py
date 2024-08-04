import os
from time import sleep
#Criar um sistema bancário com as operações : sacar, depositar, e vizualizar extrato

menu = '''
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
'''

saldo , num_saques_diarios = (0, 0)
extrato = ''
LIMITE_SAQUE = 3
LIMITE = 500.00

while True:

    opcao = input(f'{menu} Escolha uma opção: ')

    if opcao == '1':
        valor = float(input('Informw o valor do depósito: '))

        if valor > 0:
            saldo += valor
            print('Depósito realizado com sucesso')
            extrato += f'Depósito de R${valor:.2f} realizado. Saldo atual de R${saldo:.2f}\n'
        else:
            print('operação não realizada, o valor informado é inválido')
    
    elif opcao == '2':
        valor = float(input('Informe o valor a sacar: '))

        if valor <= saldo:
            saldo -= valor
            extrato += f'Saque de R${valor} realizado. Saldo atual de R${saldo:.2f}\n'
            print('Saque realizado com sucesso')
        
        else:
            print('Saldo insuficiente')
    
    elif opcao == '3':
        print(extrato)

    elif opcao == '4':
        break

    else:
        print('opção inválida!')
