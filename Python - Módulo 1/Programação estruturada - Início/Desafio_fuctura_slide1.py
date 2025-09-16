from math import ceil

pessoas = int(input('Digite quantas pessoas vão jantar no restaurante: '))
mesas = pessoas / 4
print(f'Serão necessárias {ceil(mesas)} mesas.')
