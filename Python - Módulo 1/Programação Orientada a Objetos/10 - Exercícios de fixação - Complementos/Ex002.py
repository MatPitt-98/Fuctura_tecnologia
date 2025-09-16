'''
Implemente a classe Ponto com __repr__ que mostra coordenadas.
'''

class Ponto:
    def __init__(self, nome, x, y, z):
        self.nome = nome
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'{self.nome}:\nX = {self.x}\nY = {self.y}\nZ = {self.z}'
    
ponto_1 = Ponto('Ponto 1', 5, 2, 7)
print(repr(ponto_1))