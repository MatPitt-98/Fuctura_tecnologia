'''Escreva um programa que leia a hora atual (0 a 23) e mostre uma saudação: 
00 a 11 → Bom dia 
12 a 17 → Boa tarde 
18 a 23 → Boa noite 
Se a hora for inválida, exiba "Hora inválida".'''

# da biblioteca datetime use a funcao datetime
from datetime import datetime

horario = input("Digite um horario (hh:mm): ")
print(datetime.now().time()) # datetime.now().time() -> a hora atual

# convertendo a string e capturando apenas o horario com o strptime e o atributo .time()
horario = datetime.strptime(horario, "%H:%M").time()
hora = horario.hour

if 0 <= hora < 12:
    print("Bom dia!")
elif 12 <= hora < 18:
    print("Boa tarde!")
elif 18 <= hora <= 23:
    print("Boa noite!")
else:
    print("Hora inválida!")
