# Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Instancie um objeto e imprima esses atributos.

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa_01 = Pessoas('Matheus', 27)
print(f'Olá! Me chamo {pessoa_01.nome} e tenho {pessoa_01.idade} anos.')