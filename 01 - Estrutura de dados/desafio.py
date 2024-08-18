def menu():
    menu = '''
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar usuário
    [5] - Criar conta corrente
    [6] - Exibir contas
    [7] - Sair
 
    '''
    return input(f'{menu}\nEscolha uma opção: ')


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #keyword only
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n @@@ Saldo insuficiente ! @@@')
    elif excedeu_limite:
        print('\n @@@ Você não pode sacar mais do que o valor limite @@@')
    elif excedeu_saques:
        print('\n @@@ Você não pode realizar mais saques hoje @@@')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque de R${valor:.2f}\n'
        numero_saques += 1
        print('\n === Saque realizado com sucesso ! ===')
    else:
        print('\n @@@ O valor informado não é valido @@@')

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):#positional only
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R${valor:.2f}\n'
        print('\n === Depósito realizado com sucesso ===')

    else:
        print('\n @@@ O valor informado não é valido @@@')

    return saldo, extrato
    

def exibir_extrato(saldo, /, *, extrato):#positional only and keyword only
    print('==========EXTRATO==========')
    if not extrato:
        print('\n @@@ Não foram realizadas operações @@@')
    else:
        extrato += f'Saldo atual de R${saldo:.2f}\n'
        print(extrato)
        print('====================')


def criar_usuario(lista_usuarios):
    cpf = input('Informe o cpf (somente os números): ')
    usuario = verificar_cpf(cpf, lista_usuarios)

    if usuario:
        print('\n @@@ Já existe um usuário com esse cpf @@@')
        return
    nome = input('Informe o nome do usuário: ').strip()
    data_nascimento = input('Informe a data de nascimento: ').strip()
    endereco = input('Informe o endereco (logradouro - nro - bairro - cidade/sigla do estado): ')
    lista_usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print('\n === Usuário registrado com sucesso ! ===')


def verificar_cpf(cpf, lista_usuarios):
    cpf_usuario = [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf]
    return cpf_usuario[0] if cpf_usuario else None


def criar_conta(agencia, lista_contas, numero_conta, lista_usuarios):
    cpf = input('Informe o cpf (somente os números): ')
    usuario = verificar_cpf(cpf, lista_usuarios)

    if usuario:
        print('\n === Conta criada com sucesso ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n @@@ Usuário não encontrado! operação não realizada @@@')


def exibir_contas(lista_contas):
    if not lista_contas:
        print('\n @@@ Não existem contas @@@')
        return
    for conta in lista_contas:
        contas = f'''
            Agencia:\t{conta['agencia']}\n
            Numero_conta:\t{conta['numero_conta']}\n
            Nome:\n{conta['usuario']['nome']}\n
        '''
        print(f'{contas.center(20)}')
        print('==' * 20)


def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    lista_usuarios = list()
    lista_contas = list()
    saldo = 0
    numero_saques = 0
    extrato = ''
    limite = 500

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor para depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor para sacar: '))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == '4':
            criar_usuario(lista_usuarios)
        elif opcao == '5':
            numero_conta = len(lista_contas) + 1
            conta = criar_conta(AGENCIA, lista_contas, numero_conta, lista_usuarios)
            
            if conta:
                lista_contas.append(conta)

        elif opcao == '6':
            exibir_contas(lista_contas)

        elif opcao == '7':
            break

        else:
            print('\n @@@ Opção inválida @@@')


main()