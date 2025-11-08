'''
Solicite uma temperatura em Fahrenheit e converta para Celsius. A
fórmula para conversão é: C=(F-32)x95.
C=(F-32)x59C = (F - 32) \times \frac{5}{9}
'''

temp_fahrenheit = int(input('Digite a temperatura em fahrenheit: '))
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

print(f'{temp_fahrenheit}º f convertido para graus celsius equivale a: {temp_celsius}º c')
