# Crie uma função que receba uma string e retorne a quantidade de vogais nela.

def contar_vogais(texto):
    vogais = 'aeiouáéíóúàèìòùãõâêîôûäëïöü'
    contador = 0
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    return contador

frase = 'FUCTURA TECNOLOGIA'
print(f'A quantidade de vogais na frase é {contar_vogais(frase)}')