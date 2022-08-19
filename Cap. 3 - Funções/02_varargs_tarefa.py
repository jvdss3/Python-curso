# Uso de argumentos variáveis


# TODO: Defina uma função que recebe argumentos variáveis
def adicao(base, *args):
    return sum(args)


def main():
    # TODO: Passe argumentos diferentes para o método adicao()
    print(adicao(5, 10, 15))
    print(adicao(1, 2, 3, 4, 5, 6))
    # TODO: Passe uma lista para o método adicao()
    valores = [5, 10, 15]
    print(adicao(*valores))

if __name__ == "__main__":
    main()
