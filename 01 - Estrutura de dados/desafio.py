# Separar o desafio em funcoes 
def sacar(*, saldo, valor, extrato, num_qtd_saques, LIMITE_VALOR_SAQUES): #keyword only
    qtd_saldo = valor > saldo

    limite_qtd_saques = num_qtd_saques > 3

    limite_valor_saque = valor > LIMITE_VALOR_SAQUES

    if qtd_saldo:
        print('Saldo insuficiente')

    elif limite_qtd_saques:
        print('Você atingiu o limite de saques diários')

    elif limite_valor_saque:
        print('Você não pode sacar mais do que o seu valor limite')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        num_qtd_saques += 1
    else:
        print('operação não realizada, o valor informado é inválido')
    return saldo, extrato



def depositar(saldo, valor, extrato):#positional only
    if valor < 0:
        print('operação não realizada, valor inválido')
    else:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    return saldo, extrato


def exibir_extrato(saldo, *, extrato):#positional only and keyword only
    if not extrato:
        print('Não foram realizadas movimentações')
    else:   
        extrato += f'Saldo atual de R${saldo:.2f}'
        print(extrato)


def criar_usuario(lista):
    pass


def criar_conta_corrente():
    pass


def main():
    """_summary_
    funcao que exibi e chama as outras funções
    """
    saldo = 0
    extrato = ''
    num_qtd_saques = 3
    LIMITE_VALOR_SAQUES = 500.00
    while True:

        menu = '''
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Criar usuário
        [5] - Criar conta corrente
        [6] - Sair
        '''
        print(menu)
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            valor = float(input('Informe o valor a depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
                valor = float(input('Informe o valor a sacar: '))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, num_qtd_saques=num_qtd_saques, LIMITE_VALOR_SAQUES=LIMITE_VALOR_SAQUES)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            break

main()