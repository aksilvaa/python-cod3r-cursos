palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=",")
print('Fim')

aprovados = ['Alison', 'Keuver', 'da', 'Silva']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)


dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dias in dias_semana:
    print(f' Hoje é {dias}')

for letra in set('muito legal'):
    print(letra)

for numero in set('123456789'):
    print(numero)
