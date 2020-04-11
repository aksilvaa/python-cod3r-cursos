# while True:
#     print('Vai demorar muitooo')

from random import randint

# -1,pois ele está fora das possibilidades
numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um número entre 0 e 9: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
