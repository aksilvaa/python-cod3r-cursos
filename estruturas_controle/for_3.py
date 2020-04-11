produto = {'nome': 'Caneta Chic', 'preço': 14.99,
           'importada': True, 'estoque': 793}

# property
for chave in produto:
    print(chave)

# values
for valor in produto.values():
    print(valor)

# Acessar chave e valor ao mesmo tempo
for chave, valor in produto.items():
    print(chave, '=', valor)
