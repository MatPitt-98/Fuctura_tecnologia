# Crie um método dentro da classe Carro chamado descricao() que retorne uma string com a marca e o ano do carro.

class Carros:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

    def descricao(self):
        return f'{self.modelo}... Este carro é da marca {self.marca} e é do ano {self.ano}.'

carro_01 = Carros('Jesko', 'Koenigsegg', 2020)
print(carro_01.descricao())
