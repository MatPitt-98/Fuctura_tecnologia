# Peça ao usuário para inserir um número e imprima a tabuada desse número de 1 a 10.

'''Assim
    |
    V
'''

# numero1 = int(input('Digite um número inteiro: '))
# numero2 = 1
# resultado = numero1 * numero2
# print(f'Tabuada de {numero1}: ')
# while numero2 < 11:
#     print(f'{numero1} x {numero2} = {resultado}')
#     numero2 += 1
#     resultado = numero1 * numero2

'''Ou assim
    |
    V
'''

numero1 = int(input('Digite um número inteiro: '))
print(f'Tabuada de {numero1}: ')
for numero2 in range(1, 11):
    print(f'{numero1} x {numero2} = {numero1 * numero2}')