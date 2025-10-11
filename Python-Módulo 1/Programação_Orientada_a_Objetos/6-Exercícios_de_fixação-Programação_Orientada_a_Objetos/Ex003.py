# Crie uma classe Carro com atributos marca e ano. Instancie um carro e imprima seus atributos.

class Carros:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

carro_01 = Carros('Jesko', 'Koenigsegg', 2020)
print(carro_01.modelo, carro_01.marca, carro_01.ano)