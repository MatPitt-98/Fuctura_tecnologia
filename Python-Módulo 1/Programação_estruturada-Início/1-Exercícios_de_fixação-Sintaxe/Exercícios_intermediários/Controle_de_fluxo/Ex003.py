'''Faça um programa que leia três notas de um aluno, calcule a média e escreva se o aluno está aprovado (média ≥ 7), reprovado (média < 4) ou 
em prova final (média entre 4 e 7).'''

print('Por favor, digite apenas valores entre 0 e 10.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
print(f'Sua média é {media:.1f}.')

if media >= 7 and media <= 10:
    print('Parabéns! Você passou!')
elif media >= 4 and media < 7:
    print('Você precisa fazer a prova final!')
elif media < 4 and media >= 0:
    print('Reprovado! Estude mais!')
else:
    print('Você digitou valores inválidos, por favor, digite apenas valores entre 0 e 10.')