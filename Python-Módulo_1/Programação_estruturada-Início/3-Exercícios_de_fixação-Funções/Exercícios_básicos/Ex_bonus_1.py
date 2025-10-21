# Escreva uma função que receba um valor inteiro e mostre cada um dos seus dígitos

def digitos_numero():
    num = int(input('Digite um número inteiro de 0 a 9999999: '))
    unidade = num // 1 % 10
    dezena = num // 10 % 10
    centena = num // 100 % 10
    milhar = num // 1000 % 10
    dezena_de_milhar = num // 10000 % 10
    centena_de_milhar = num // 100000 % 10
    milhao = num // 1000000 % 10
    print(f'Milhão: {milhao}\nCentena de milhar: {centena_de_milhar}\nDezena de milhar: {dezena_de_milhar}\nMilhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {unidade}')

digitos_numero()