# Crie um programa que leia o valor de um empréstimo, a taxa de juros mensal e o número de meses para calcular o valor da parcela mensal.

valor_emprestimo = float(input('Digite o valor do empréstimo: R$'))
taxa_juros = float(input('Digite a taxa de juros mensal: R$'))
meses = int(input('Digite a quantidade de meses: '))
valor_total = valor_emprestimo + (valor_emprestimo * (taxa_juros / 100) * meses)

valor_parcela = valor_total / meses
print(f'O valor da parcela mensal é de R${valor_parcela:.2f}.')