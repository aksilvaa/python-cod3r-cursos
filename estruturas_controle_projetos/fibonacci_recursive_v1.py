#! python


def fibonacci(quantidade, sequencia=(0, 1)):
    # Condição de Parada
    if len(sequencia) == quantidade:
        return sequencia
    # Criação de nova tupla responsável por unir os resultados das tuplas.
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
