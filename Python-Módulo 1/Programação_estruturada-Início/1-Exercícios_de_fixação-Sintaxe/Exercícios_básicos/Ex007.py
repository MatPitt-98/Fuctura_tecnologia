# Crie um programa que leia o peso de uma encomenda (em kg) e calcule o valor do frete, considerando R$ 5,00 por kg.

peso_encomenda = float(input('Digite o peso da encomenda em kg: '))
print(f'O preço do frete é de R${peso_encomenda * 5:.2f}.')
