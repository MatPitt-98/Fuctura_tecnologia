# Escreva um programa que leia o número do mês (1 a 12) e diga quantos dias ele tem (considerando ano não bissexto).

mes = int(input('Digite um mês (1 a 12) para saber quantos dias ele tem: '))
if mes == 1:
    print('Janeiro tem 31 dias.')
elif mes == 2:
    print('Fevereiro tem 28 dias.')
elif mes == 3:
    print('Março tem 31 dias.')
elif mes == 4:
    print('Abril tem 30 dias.')
elif mes == 5:
    print('Maio tem 31 dias.')
elif mes == 6:
    print('Junho tem 30 dias.')
elif mes == 7:
    print('Julho tem 31 dias.')
elif mes == 8:
    print('Agosto tem 31 dias.')
elif mes == 9:
    print('Setembro tem 30 dias.')
elif mes == 10:
    print('Outubro tem 31 dias.')
elif mes == 11:
    print('Novembro tem 30 dias.')
elif mes == 12:
    print('Dezembro tem 31 dias.')
else:
    print('Por favor, digite um número válido para o programa (de 1 a 12).')