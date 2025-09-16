# Crie um programa que leia o preço à vista de um produto e o número de parcelas para calcular o valor de cada prestação, considerando juros simples de 2% ao mês.

preco_a_vista = float(input('Digite o preço a vista do produto: '))
numero_parcelas = int(input('Digite o número de parcelas: '))
taxa_juros = 0.02
valor_total = preco_a_vista * (1 + taxa_juros * numero_parcelas)
valor_parcela = valor_total / numero_parcelas
print(f'O valor de cada parcela é R${valor_parcela:.2f}.')
