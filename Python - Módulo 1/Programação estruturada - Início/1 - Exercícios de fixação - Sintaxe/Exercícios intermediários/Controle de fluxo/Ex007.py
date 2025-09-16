'''
Escreva um programa que leia dois números inteiros e um operador aritmético (+, -, *, /), execute a operação e mostre o resultado.
Se o operador for inválido, exiba mensagem de erro.
'''

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite mais um número inteiro: '))
operador = input('Digite um dos seguintes operadores aritméticos, +, -, *, /: ')
if operador == '+':
    print(f'{num_1} + {num_2} = {num_1 + num_2}')
elif operador == '-':
    print(f'{num_1} - {num_2} = {num_1 - num_2}')
elif operador == '*':
    print(f'{num_1} x {num_2} = {num_1 * num_2}')
elif operador == '/':
    print(f'{num_1} / {num_2} = {num_1 / num_2}')
else:
    print('Por favor, digite um operador válido.')