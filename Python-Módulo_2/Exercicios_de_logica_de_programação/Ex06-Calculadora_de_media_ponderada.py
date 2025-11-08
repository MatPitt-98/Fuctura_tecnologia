'''
Solicite ao usuário as notas de três provas e seus respectivos 
pesos. Calcule a média ponderada das notas e informe se o aluno 
foi aprovado (média >= 7), reprovado (média < 4) ou em 
recuperação (média entre 4 e 7).
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'\nMédia: {media:.2f}\n')

if media >= 7:
    print('Parabéns! Você foi aprovado!')

elif media >= 4 and media < 7:
    print('Em recuperação...')

elif media < 4:
    print('Você está reprovado, estude mais!')
