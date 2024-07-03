import logging
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

logging.basicConfig(level=logging.INFO)

LIMITE_SAQUES = 3
LIMITE = 500

console = Console()

def mostrar_menu():
    console.print("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
""", style="bold cyan")
    return Prompt.ask("Selecione uma opção", choices=["d", "s", "e", "q"], default="q").strip().lower()

def obter_valor_float(mensagem):
    while True:
        try:
            return float(Prompt.ask(mensagem))
        except ValueError:
            console.print("Valor inválido. Por favor, insira um número.", style="bold red")

def depositar(saldo, extrato):
    valor = obter_valor_float("Informe o valor do depósito: ")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        logging.info(f"Depósito: R$ {valor:.2f}")
        console.print(f"Depósito de R$ {valor:.2f} realizado com sucesso!", style="bold green")
    else:
        console.print("Operação falhou! O valor informado é inválido.", style="bold red")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = obter_valor_float("Informe o valor do saque: ")

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        console.print("Operação falhou! Você não tem saldo suficiente.", style="bold red")
    elif excedeu_limite:
        console.print("Operação falhou! O valor do saque excede o limite.", style="bold red")
    elif excedeu_saques:
        console.print("Operação falhou! Número máximo de saques excedido.", style="bold red")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        logging.info(f"Saque: R$ {valor:.2f}")
        console.print(f"Saque de R$ {valor:.2f} realizado com sucesso!", style="bold green")
    else:
        console.print("Operação falhou! O valor informado é inválido.", style="bold red")
    
    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    console.print("\n================ EXTRATO ================", style="bold magenta")
    if not extrato:
        console.print("Não foram realizadas movimentações.", style="bold yellow")
    else:
        console.print(extrato, style="bold white")
    console.print(f"\nSaldo: R$ {saldo:.2f}", style="bold green")
    console.print("==========================================", style="bold magenta")

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    
    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE, LIMITE_SAQUES)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            console.print("Obrigado por utilizar o sistema bancário! Até a próxima!", style="bold cyan")
            break
        else:
            console.print("Operação inválida, por favor selecione novamente a operação desejada.", style="bold red")

if __name__ == "__main__":
    main()
