# Escreva um programa que leia uma letra do alfabeto e diga se é vogal ou consoante.

letra = input('Digite um letra: ').lower()
print(f'Você digitou: {letra}.')
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'õ', 'â', 'ê', 'î', 'ô', 'û', 'ä', 'ë', 'ï', 'ö', 'ü']
if letra in vogais:
    print(f'A letra {letra} é uma vogal.')
elif not letra.isalpha():
    print('Você não digitou uma letra.')
else:
    print(f'A letra {letra} é uma consoante.')