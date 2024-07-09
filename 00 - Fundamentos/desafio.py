menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferir
[l] Limite de Saques
[q] Sair

=> """

# Variáveis Globais
usuarios = []


def criar_usuario(nome, cpf):
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0
        }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def depositar(usuario, valor):
    if valor > 0:
        usuario["saldo"] += valor
        usuario["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return usuario


def sacar(usuario, valor):
    excedeu_saldo = valor > usuario["saldo"]
    excedeu_limite = valor > usuario["limite"]
    excedeu_saques = usuario["numero_saques"] >= 3

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        usuario["saldo"] -= valor
        usuario["extrato"] += f"Saque: R$ {valor:.2f}\n"
        usuario["numero_saques"] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return usuario


def exibir_extrato(usuario):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not usuario["extrato"] else usuario["extrato"])
    print(f"\nSaldo: R$ {usuario['saldo']:.2f}")
    print("==========================================")


def transferir(usuario, valor):
    if valor > 0 and valor <= usuario["saldo"]:
        usuario["saldo"] -= valor
        usuario["extrato"] += f"Transferência: R$ {valor:.2f}\n"
        print("Transferência realizada com sucesso!")
    elif valor > usuario["saldo"]:
        print("Operação falhou! Você não tem saldo suficiente.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return usuario


def mostrar_limite_saques(usuario):
    saques_restantes = 3 - usuario["numero_saques"]
    print(f"Você pode realizar mais {saques_restantes} saque(s) hoje.")


def main():
    while True:
        opcao = input(menu)

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                valor = float(input("Informe o valor do depósito: "))
                usuario = depositar(usuario, valor)
            else:
                print("Usuário não encontrado.")

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                valor = float(input("Informe o valor do saque: "))
                usuario = sacar(usuario, valor)
            else:
                print("Usuário não encontrado.")

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                exibir_extrato(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "t":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                valor = float(input("Informe o valor da transferência: "))
                usuario = transferir(usuario, valor)
            else:
                print("Usuário não encontrado.")

        elif opcao == "l":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                mostrar_limite_saques(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "q":
            print("Você escolheu sair! Obrigado por utilizar nosso banco.")
            break

        else:
            print(
                """ Operação inválida,
                 por favor selecione novamente a operação desejada."""
            )


if __name__ == "__main__":
    nome = input("Informe o nome do usuário para criar uma conta: ")
    cpf = input("Informe o CPF do usuário: ")
    criar_usuario(nome, cpf)
    main()
