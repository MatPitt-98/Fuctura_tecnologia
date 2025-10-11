'''Crie um programa que leia a altura e largura de uma parede (em metros), calcule sua área e determine a quantidade de tinta necessária para pintá-la 
considerando que cada litro cobre 2m².'''

altura_parede = float(input('Digite a altura da parede em metros: '))
largura_parede = float(input('Digite a largura da parede em metros: '))
area_parede = altura_parede * largura_parede
print(f'A parede tem uma área de {area_parede:.2f}m² e serão necessários {area_parede / 2:.2f} litros de tinta para pintá-la.')
