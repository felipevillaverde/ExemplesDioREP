import os
from time import sleep

menu = '''
[1] - Depositar
[2] - Sacar
[3] - extrato
[4] - sair
'''

saldo = 0
num_saques_dia = 0
extrato = ''
LIMITE_SAQUE_DIARIO = 3
LIMITE = 500.00

while True:
  #usei esta função da biblioteca os para estar limpando o terminal ao final de cada iteração
  os.system('cls' if os.name == 'nt' else 'clear')

  msg = 'Olá, Seja bem vindo!'

  print(f'{msg.center(50, "=")}')
  opcao = input(f'{menu} Escolha uma opção: ')

  if opcao == '1':
    valor = float(input('Informe o valor do depósito: '))

    if valor > 0:
      saldo += valor
      extrato += f'Depósito: R$ {valor:.2f}. Saldo total de R${saldo:.2f}\n'
      print('Depoisitado com sucesso!')
      sleep(2)

    else:
      print('O valor informado é inválido!')
      sleep(2) 
  
  elif opcao == '2':
    valor = float(input('Informe o valor do Saque: '))

    # modifiquei as minhas condicoes criando variaveis para cada uma delas assim como no codigo do professor Guilherme pois achei  mais legivel como codigo
    qtd_saldo = valor > saldo

    limite_qtd_saques = num_saques_dia >= LIMITE_SAQUE_DIARIO

    limite_valor_saque = valor > LIMITE

    if qtd_saldo:
      print('Saldo insuficiente.')
      sleep(2)

    elif limite_qtd_saques:
      print('Limite de saques diários atingido.')
      sleep(2)
      
    elif limite_valor_saque:
      print('Valor de saque excede o limite.')
      sleep(2)
      
    else:
      saldo -= valor 
      num_saques_dia += 1
      extrato += f'Saque: R$ {valor:.2f}. Saldo total de R${saldo:.2f}\n'
      print('Saque realizado com sucesso.')
      sleep(2)

  elif opcao == '3':
    if not extrato:
      print('Não há foram realizadas movimentações')
      sleep(2)
    else:
      print(extrato)
    print('Pressione enter para continuar: ')
    input()

  elif opcao == '4':
    print('Obrigado por usar nosso banco!')
    break

  else:
    print('opção inválida, tente novamente')
    sleep(2)