'''
Crie um programa que gerencie o saldo de uma conta bancária. O
usuário pode fazer depósitos e saques, e o programa deve exibir o
saldo atual após cada operação.
'''

saldo = 0
print('Digite o número de acordo com o que deseja: ')

while True:

    opcao = input('1 - Depositar\n2 - Sacar\n3 - Verificar Saldo\n4 - Sair\n')

    if opcao == '1':
        depositar = float(input('Digite o valor a ser depositado: R$'))
        saldo += depositar

    elif opcao == '2':
        sacar = float(input('Digite o valor a ser sacado: R$'))
        if sacar > saldo:
            print('Saldo insuficiente!')
        else:
            saldo -= sacar

    elif opcao == '3':
        print(f'O saldo atual é de: R${saldo:.2f}')

    elif opcao == '4':
        print('Programa encerrado')
        break

    else:
        print('Por favor digite algo válido para o programa.')
