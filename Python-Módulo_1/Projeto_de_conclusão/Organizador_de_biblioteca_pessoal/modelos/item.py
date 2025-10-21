class Item:
    def __init__(self, titulo, autor, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
    
    ## getter de titulo -- método de acesso indireto
    @property # definir que é um getter
    def titulo(self):
        return self.__titulo
    
    ## setter de titulo
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str) and titulo.strip():
            self.__titulo = titulo
        else:
            print("Valor inválido para título!")
    ## getter de autor
    @property
    def autor(self):
        return self.__autor

    ## setter de autor
    @autor.setter
    def autor(self, autor):
        if isinstance(autor, str) and autor.strip():
            self.__autor = autor
        else:
            print("Valor inválido para autor!")
    ## getter de categoria
    @property
    def categoria(self):
        return self.__categoria
    
    ## setter de categoria
    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, str) and categoria.strip():
            self.__categoria = categoria
        else:
            print("Valor inválido para categoria!")

    def __str__(self):
        return f"Título: {self.__titulo} \nAutor: {self.__autor} \nCategoria: {self.__categoria}"