from repositorios.item_repositorio import Repositorio
from servicos.item_servico import Servico

def exibir_menu():
    print('\n-_-_- Programa Principal -_-_-')
    print('1 - Adicionar Item')
    print('2 - Listar Itens')
    print('3 - Listar por Categoria')
    print('4 - Remover Item por Título')
    print('0 - Sair do programa')
    return input('Escolha uma opção: ')

def main():
    repositorio = Repositorio()
    servico = Servico(repositorio)

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            titulo = input('Digite o Título:')
            autor = input('Digite o Autor: ')
            categoria = input('Digite a Categoria: ')
            servico.adicionar_item(titulo, autor, categoria)

        elif opcao == '2':
            servico.listar_itens()

        elif opcao == '3':
            categoria = input('Informe a categoria: ')
            servico.listar_por_categoria(categoria)

        elif opcao == '4':
            titulo = input('Informe o título do item para remover: ')
            servico.remover_por_titulo(titulo)

        elif opcao == '0':
            print('Encerrando a aplicação...')
            break

        else:
            print('Opção Inválida!')

if __name__ == '__main__':
    main()