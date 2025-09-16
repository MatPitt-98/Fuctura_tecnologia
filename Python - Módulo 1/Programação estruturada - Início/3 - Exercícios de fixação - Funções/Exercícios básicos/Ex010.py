''' Crie uma função que receba dois números e um operador ('+', '-', '*', '/') e 
retorne o resultado da operação matemática, tratando casos de divisão por zero. '''

def calculo():
    a = float(input('Digite um número: '))
    b = float(input('Digite outro número: '))
    operador = input('Digite o operador aritmético: ')
    if operador == '+':
        resultado = a + b
    elif operador == '-':
        resultado = a - b
    elif operador == '*':
        resultado = a * b
    elif operador == '/':
        if b != 0:
            resultado = a / b
        else:
            resultado = 'Não se pode dividir por zero!'
    else:
        resultado = 'Por favor digite algo válido para o programa.'
    return resultado

print(calculo())