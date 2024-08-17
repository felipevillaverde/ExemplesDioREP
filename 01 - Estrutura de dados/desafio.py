# Separar o desafio em funcoes 
def sacar(*, saldo, valor, extrato, num_saques, LIMITE_SAQUES): #keyword only
    LIMITE_SAQUES = 500.00
    valor = float(input('Informe o valor a sacar: '))

    qtd_saldo = valor > saldo

    limite_qtd_saques = num_saques > 3

    limite_valor_saque = valor > LIMITE_SAQUES

    if qtd_saldo:
        print('Saldo insuficiente')

    elif limite_qtd_saques:
        print('Você atingiu o limite de saques diários')

    elif limite_valor_saque:
        print('Você não pode sacar mais do que o seu valor limite')

    else:
        saldo -= valor


def depositar(saldo, valor, extrato):#positional only
    valor = float(input('Informe o valor a depositar: '))
    if valor < 0:
        print('operação não realizada, valor inválido')
    else:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}. Saldo total de R${saldo:.2f}\n'
    return saldo, extrato


def extrato(saldo, *, extrato):#positional only and keyword only
    print('Não há foram realizadas movimentações' if not extrato else extrato)


def criar_usuario(lista):
    pass


def criar_conta_corrente():
    pass


def main():
    """_summary_
    funcao que exibi e chama as outras funções
    """
    while True:
        menu = '''
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Criar usuário
        [5] - Criar conta corrente
        [6] - Sair
        '''
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            pass
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            break
