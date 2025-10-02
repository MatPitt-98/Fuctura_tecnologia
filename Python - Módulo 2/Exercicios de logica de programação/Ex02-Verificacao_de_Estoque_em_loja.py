'''
Crie um programa que gerencie o estoque de uma loja. O programa deve permitir adicionar ou retirar produtos, além de verificar a 
quantidade atual de determinado produto. Use um dicionário para armazenar os produtos e suas quantidades.
'''

produtos_em_estoque = {}
while True:
    acao = int(input('\n1 - adicionar produto e quantidade\n2 - retirar produto\n3 - verificar quantidade de determinado produto ou todos os produtos\n4 - sair\n'))
    if acao == 1:
        produto = input('\nDigite o produto a ser adicionado: ').lower()
        quantidade = int(input('Digite a quantidade desse produto: '))
        produtos_em_estoque[produto] = quantidade
        
    elif acao == 2:
        produto_para_retirar = input('Digite o produto para ser retirado: ').lower()
        quantidade_para_retirar = int(input('Digite a quantidade desse produto para ser retirado: '))
        if produto_para_retirar in produtos_em_estoque:
            if quantidade_para_retirar > produtos_em_estoque[produto_para_retirar]:
                print(f'\nQuantidade desejada insuficiente no estoque!\nQuantidade atual de {produto_para_retirar} no estoque: {produtos_em_estoque[produto_para_retirar]}.')
            else: 
                produtos_em_estoque[produto_para_retirar] -= quantidade_para_retirar
                print(f'\nRetiradas {quantidade_para_retirar} unidades de {produto_para_retirar} do estoque.\nQuantidade atual de {produto_para_retirar} no estoque: {produtos_em_estoque[produto_para_retirar]}.')
            
        elif produto_para_retirar not in produtos_em_estoque:
            print(f'\nO estoque não possui o produto {produto_para_retirar}!\nProdutos no estoque: {produtos_em_estoque}')
        else:
            print('Por favor, digite algo válido para o programa!')

    elif acao == 3:
        verificacao = input('\nDigite o produto específico desejado ou "todos" para ver todo o estoque: ').lower()
        if verificacao in produtos_em_estoque:
            print(f'\nQuantidade de {verificacao}: {produtos_em_estoque[verificacao]}.')
        elif verificacao == 'todos':
            print('\nTodos os produtos no estoque:', produtos_em_estoque)
        else:
            print('\nProduto não encontrado!')

    elif acao == 4:
        print('Programa encerrado.')
        break

    else:
        print('Por favor, digite algo válido para o programa!')
        break
    