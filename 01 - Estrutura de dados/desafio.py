# Separar o desafio em funcoes 
def sacar(*, saldo, valor, extrato, num_saques, limite_saques, ): #keyword only

    pass


def depositar(saldo, valor, extrato):#positional only
    pass


def extrato(saldo, *, extrato):#positional only and keyword only
    pass


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
