'''
Crie uma classe Animal com um método falar() que imprima "Animal falando". Crie uma classe Cachorro que herde de Animal e 
sobrescreva falar() para imprimir "Au au!".
'''

class Animal:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def falar(self):
        print('Animal falando...')

animal_1 = Animal('Mufasa', 1.6)
print(f'{animal_1.nome} tem {animal_1.altura} de altura:')
animal_1.falar()

print('')

class Cachorro(Animal):
    def falar(self):
        print('Au au!')

cachorro_1 = Cachorro('Amy', 0.8)
print(f'{cachorro_1.nome} tem {cachorro_1.altura} de altura:')
cachorro_1.falar()