# Crie um programa que leia o consumo mensal de água de uma residência (em litros) e calcule o valor da conta, considerando que cada litro custa R$ 0,02.

consumo_mensal = int(input('Digite o consumo mensal de água em litros: '))
valor_conta = consumo_mensal * 0.02
print(f'O valor da conta é de {valor_conta:.2f}.')
