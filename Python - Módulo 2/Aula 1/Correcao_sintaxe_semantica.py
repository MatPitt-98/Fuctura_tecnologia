def analisar_lista_compras():
    itens = []
    precos = []

    print("=== ANALISADOR DE LISTA DE COMPRAS ===")
    print("Digite os itens e seus preços (digite 'fim' para terminar)")

    while True:
        item = input("Nome do item: ")
        if item.lower() == 'fim':  # Corrigido: == e :
            break

        try:
            preco = input(f"Preço de {item}: R$ ")
            itens.append(item)
            precos.append(float(preco))  # Com tratamento de erro
        except ValueError:
            print("Erro: Digite um preço válido!")
            continue

    # Verificar se a lista não está vazia
    if len(itens) == 0:
        print("\nNenhum item foi adicionado!")
        return

    # Cálculos (agora seguros)
    total = sum(precos)
    media = total / len(precos)
    item_mais_caro = itens[precos.index(max(precos))]

    # Exibir resultados
    print("\n--- RESULTADOS ---")
    print(f"Total de itens: {len(itens)}")
    print(f"Valor total: R$ {total:.2f}")
    print(f"Preço médio: R$ {media:.2f}")
    print(f"Item mais caro: {item_mais_caro} (R$ {max(precos):.2f})")

    # Itens com preço acima da média
    print("\nItens com preço acima da média:")
    for i in range(len(itens)):
        if precos[i] > media:  # Corrigido: adicionado :
            print(f"- {itens[i]}: R$ {precos[i]:.2f}")


# Chamar a função
analisar_lista_compras()
