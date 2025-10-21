'''Faça um programa que receba uma sequência de números inteiros e imprima o maior e o menor número da sequência.
A entrada termina quando o usuário digitar o número zero.'''

sequencia = []
while 0 not in sequencia:
    numero = int(input('Digite quaisquer números inteiros, quando terminar digite 0 para sair: '))
    sequencia.append(numero)
    sequencia.sort()
    print(f'Números digitados: {sequencia}')

print(f'O maior número da lista é {sequencia[-1]} e o menor é {sequencia[0]}.')
print('Saindo...')