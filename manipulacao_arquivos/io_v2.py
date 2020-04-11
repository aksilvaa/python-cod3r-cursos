#! python
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()

# Streaming de Dados -- Dados são enviados parcialmente
