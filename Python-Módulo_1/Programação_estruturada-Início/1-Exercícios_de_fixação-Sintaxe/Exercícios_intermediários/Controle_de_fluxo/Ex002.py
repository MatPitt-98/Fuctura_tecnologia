# Escreva um programa que leia dois números inteiros do usuário e diga qual é o maior, o menor ou se são iguais.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
if num1 == num2:
    print('Os números são iguais.')
elif num1 > num2:
    print(f'O número {num1} é maior do que o número {num2}.')
else:
    print(f'O número {num1} é menor do que o número {num2}.')