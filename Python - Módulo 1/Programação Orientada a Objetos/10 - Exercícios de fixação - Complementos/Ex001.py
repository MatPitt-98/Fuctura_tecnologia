'''
Crie uma classe Livro com método __str__ para retornar o título formatado.
'''

class Livro:
    def __init__(self, titulo, qtd_paginas):
        self.titulo = titulo
        self.qtd_paginas = qtd_paginas

    def __str__(self):
        return f'Título: {self.titulo}\nQuantidade de páginas: {self.qtd_paginas}'

livro_1 = Livro('Assassins Creed', 305)
print(livro_1)