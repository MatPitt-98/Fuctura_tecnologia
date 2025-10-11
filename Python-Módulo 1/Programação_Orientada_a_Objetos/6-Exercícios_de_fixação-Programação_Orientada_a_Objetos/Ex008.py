# Crie uma classe Retangulo com atributos largura e altura. Adicione um método que calcule e retorne a área.

class retangulos:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

retangulo1 = retangulos(3, 9)
print(retangulo1.area())