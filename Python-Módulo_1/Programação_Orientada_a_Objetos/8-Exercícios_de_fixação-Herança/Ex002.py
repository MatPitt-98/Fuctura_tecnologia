'''
Crie uma classe Veiculo com atributos marca e ano. Crie uma classe Carro que herde de Veiculo e 
adicione um atributo modelo. Instancie e imprima todos os atributos.
'''

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

barco_1 = Veiculo('Marca de barcos', 2010)
print(barco_1.marca, barco_1.ano)

print('')

class Carro(Veiculo):
    def __init__(self, marca, ano, modelo):
        super().__init__(marca, ano)
        self.modelo = modelo

carro_1 = Carro('Ferrari', 2013, 'LaFerrari')
print(carro_1.marca, carro_1.ano, carro_1.modelo)