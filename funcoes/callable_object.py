#! python


class Potencia:
    # Calcula uma potencia específica __init__ = Contructor

    def __init__(self, expoente):
        self.expoente = expoente

    # Metodo utilizado quando voce utiliza um objeto como uma função
    def __call__(self, base):
        return base ** self.expoente


if __name__ == "__main__":
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'5² => {cubo(5)}')
        print(Potencia(4)(2))
