# Crie um programa que leia a distância percorrida por um carro (em km) e o tempo gasto (em horas), e calcule sua velocidade média em m/s.

distancia = float(input('Digite a distância percorrida pelo carro em kilômetros: '))
tempo = float(input('Digite o tempo gasto em horas: '))
metros = distancia * 1000
segundos = tempo * 3600
velocidade_media = metros / segundos

print(f'A velocidade média foi de {velocidade_media:.2f} m/s.')
