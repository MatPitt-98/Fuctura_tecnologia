'''
Solicite ao usuário o valor de um empréstimo, a taxa de juros anual e o período de tempo (em anos). Calcule e imprima o valor dos 
juros simples e o valor total a ser pago no final. J = c * i * t          M = C * (1 + i * t)
'''
print('Calculadora de juros simples')
print('')

emprestimo = float(input('Digite o valor do empréstimo: R$'))
taxa_juros_anual = float(input('Digite a taxa de juros anual (%): ')) / 100
tempo_em_anos = int(input('Digite o tempo em anos: '))
juros_simples = emprestimo * taxa_juros_anual * tempo_em_anos
montante = emprestimo * (1 + taxa_juros_anual * tempo_em_anos)

print(f'Você irá pagar R${juros_simples:.2f} de juros simples.')
print(f'O total a pagar é de R${montante:.2f}')
