def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(66, 100):
        return 'Melhot Idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade Inválida'


if __name__ == '__main__':
    idades = (17, 0, 35, 87, 113, -2)
    for idade in idades:
        print(f'{idade}: {faixa_etaria(idade)}')
