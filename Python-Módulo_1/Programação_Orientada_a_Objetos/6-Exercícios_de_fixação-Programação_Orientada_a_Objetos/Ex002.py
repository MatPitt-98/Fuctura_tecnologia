# Adicione um método apresentar() à classe Pessoa que imprima uma mensagem com o nome e idade do objeto.

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá me chamo {self.nome} e tenho {self.idade} anos.'
    
pessoa_01 = Pessoas('Matheus', 27)
pessoa_02 = Pessoas('Caio', 35)
print(pessoa_01.apresentar())