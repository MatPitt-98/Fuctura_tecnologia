from modelos.item import Item

class Servico:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def adicionar_item(self, titulo, autor, categoria):
        if not titulo or not autor or not categoria:
            print('Todos os campos devem ser preenchidos!')
            return
    
        item = Item(titulo, autor, categoria)
        self.repositorio.adicionar_item(item)
        print('Item adicionado com sucesso!')

    def listar_itens(self):
        lista_itens = self.repositorio.listar_itens()
        if lista_itens:
            print('--- Lista de Itens ---')
            for item in lista_itens:
                print(item)
            print('--- --- --- --- --- ---')
        else:
            print('Não há itens cadastrados.')

    def listar_por_categoria(self, categoria):
        lista_itens = self.repositorio.listar_por_categoria(categoria)
        if lista_itens:
            print(f'--- Lista da categoria {categoria} ---')
            for item in lista_itens:
                print(item)
            print('--- --- --- --- --- ---')
        else:
            print(f'Não há itens cadastrados na categoria {categoria}.')

    def remover_por_titulo(self, titulo):
        removido = self.repositorio.remover_por_titulo(titulo)
        if removido:
            print('item removido com secesso!')
        else:
            print('Item não encontrado.')