# Crie uma classe Animal com método mover(). Crie classes Cachorro e Passaro que herdem de Animal e sobrescrevam mover() com mensagens específicas.

class Animal:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def mover(self):
        print('Animal andando...')

animal_1 = Animal('Simba', 1.6)
animal_1.mover()

class Cachorro(Animal):

    def mover(self):
        print('Cachorro andando...')

cachorro_1 = Cachorro('Aria', 1)
cachorro_1.mover()

class Passaro(Animal):

    def mover(self):
        print('Pássaro andando...')

passaro_1 = Passaro('Pica-Pau', 0.2)
passaro_1.mover()