import textwrap

nome_banco = "Banco DEV"
nome_bot = "Aliko"
idade_banco = 35

def menu_principal():
    menu = f"""
BBBB    AAAAAA   NN     N    CCCCC   OOOOO        DDDD    EEEEEEE  V     V
B   B   A    A   N N    N   C       O     O       D   D   E        V     V
BBBB    A    A   N  N   N  C        O     O       D    D  E        V     V
B   BB  AAAAAA   N   N  N  C        O     O       D    D  EEEE      V   V
B    B  A    A   N   N  N   C       O     O       D   D   E          V V
BBBBB   A    A   N    NN     CCCCC   OOOOO        DDDD    EEEEEEE     V

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  MENU  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Olá! Eu sou a {nome_bot}. Seja bem-vindo ao {nome_banco}!
Estamos no mercado há mais de {idade_banco} anos!
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova conta
[5]\tListar contas
[6]\tNovo usuário
[q]\tSair
"""
    print(textwrap.dedent(menu))
    return input("Escolha uma opção: ")

def depositar(saldo, valor, extrato):
    if valor > 0:
        confirmar_deposito = input(f"Tem certeza que deseja depositar o valor R${valor:.2f}? (Sim/Não): ")
        if confirmar_deposito.lower() == "sim":
            saldo += valor
            extrato += f"Depósito de R${valor:.2f} realizado com sucesso.\n"
            print("Valor depositado com sucesso!")
        else:
            print("Depósito cancelado.")
    else:
        print("Valor informado inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Desculpe, saldo insuficiente!")
    elif excedeu_limite:
        print("O valor limite para saque é de R$500,00.")
    elif excedeu_saques:
        print("Você não pode realizar mais saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R${valor:.2f} realizado com sucesso.\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor informado inválido")

    return saldo, extrato, numero_saques

def ver_extrato(saldo, /, *, extrato):
    print("\n-------------------------- EXTRATO --------------------------")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("-------------------------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário atrelado a este CPF!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 1500
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu_principal()

        if opcao == "1":
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_DE_SAQUES,
            )

        elif opcao == "3":
            ver_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao.lower() == "q":
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
