#! python

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
    # Strip é utilizado para retiarr algum elemento especifico da string,
    #  por exemplo espaços vazios
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo foi fechado')

# Streaming de Dados -- Dados são enviados parcialmente
