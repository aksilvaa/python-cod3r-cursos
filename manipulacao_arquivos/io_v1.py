#! python
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    # * Pega todos os valores dentro da lista
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
