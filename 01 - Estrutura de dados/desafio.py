# Separar o desafio em funcoes 

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #keyword only
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print('\n@@@ Saldo insuficiente. @@@')

    elif excedeu_limite:
        print('\n@@@ Você atingiu o limite de saques diários. @@@')

    elif excedeu_saques:
        print('\n@@@ Você não pode sacar mais do que o seu valor limite. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso ! ===')
    else:
        print('\n @@@ Operação não realizada, o valor informado é inválido. @@@')

    return saldo, extrato



def depositar(saldo, valor, extrato, /):#positional only
    if valor < 0:
        print('\n @@@ Operação não realizada, valor inválido @@@')
    else:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('\n=== Depósito realizada com sucesso! ===')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):#positional only and keyword only
    if not extrato:
        print('Não foram realizadas movimentações')
    else:   
        extrato += f'Saldo atual de: R${saldo:.2f}'
        print(extrato)


def criar_usuario(lista_usuarios):
    cpf = input('Informe o cpf (somente o número): ').replace('.', '').strip()
    usuario = filtar_usuarios(cpf, lista_usuarios)

    if usuario:
        print('\n @@@ Já existe um usuário com esse cpf @@@')
        return
    nome = input('Informe o nome completo: ').strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input('Informe o endereco (logradouro - nro - bairro - cidade/sigla - estado)')
    lista_usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})

    print('=== Usuário criado com sucesso ! ===')


def criar_conta_corrente(agencia, num_conta, lista_usuarios):
    cpf = input('Informe o cpf (somente o número): ').replace('.', '').strip()
    usuario = filtar_usuarios(cpf, lista_usuarios)
    if usuario:
        print('=== Conta criada com sucesso ! ===')
        return {'agencia': agencia, 'numero_conta': num_conta, 'usuario': usuario}
    
    print('\n @@@ Usuário não encontrado, Fluxo de ciação de conta encerrado ! @@@')


def filtar_usuarios(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f'''
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 30)
        print(linha)



def main():
    """_summary_
    funcao que exibi e chama as outras funções
    """
    lista_usuarios = list()
    lista_contas = list()
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    while True:

        menu = '''
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Criar usuário
        [5] - Criar conta corrente
        [6] - Listar contas
        [7] - Sair
        '''
        print(menu)
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            valor = float(input('Informe o valor a depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
                valor = float(input('Informe o valor a sacar: '))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(lista_usuarios)

        elif opcao == '5':
            numero_conta = len(lista_contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, lista_usuarios)

            if conta:
                lista_contas.append(conta)
        elif opcao == '6':
            listar_contas(lista_contas)
        elif opcao == '7':
            break

main()
