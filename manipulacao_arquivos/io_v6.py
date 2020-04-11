#! python

# Cria o Arquivo Pessoas.txt após efetuar a leitura do csv

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=(saida))
    # Strip é utilizado para retiarr algum elemento especifico da string,
    #  Por exemplo espaços vazios

if arquivo.closed:
    print('Arquivo foi fechado')

if saida.closed:
    print('Arquivo de saída já foi fechado!')
