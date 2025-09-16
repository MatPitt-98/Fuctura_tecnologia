# Escreva um programa que leia a idade de uma pessoa e diga se ela pode votar ou não, considerando as regras brasileiras para voto obrigatório e facultativo.

idade = int(input('Digite a sua idade: '))
if idade >= 16:
    print('Você pode votar.')
else:
    print('Você ainda não pode votar.')