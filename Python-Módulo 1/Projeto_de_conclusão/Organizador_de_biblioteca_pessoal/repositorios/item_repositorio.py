class Repositorio:
    def __init__(self):
        self.__itens = []
    
    def adicionar_item(self, item):
        self.__itens.append(item)
    
    def listar_itens(self):
        return self.__itens
    
    def listar_por_categoria(self, categoria):
        return [item for item in self.__itens \
                if item.categoria.lower() == categoria.lower()]
        # resultado = []

        # for item in self.__itens:
        #     if item.categoria.lower() == categoria.lower():
        #         resultado.append(item)

        # return resultado

    def remover_por_titulo(self, titulo):
        for item in self.__itens:
            if item.titulo.lower() == titulo.lower():
                self.__itens.remove(item)
                return True
        return False