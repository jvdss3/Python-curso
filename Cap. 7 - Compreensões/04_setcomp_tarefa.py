# Usando set comprehensions


def main():
    # Definindo uma lista de temperaturas
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: Crie um set com as temperaturas em Fahrenheit
    # Dica: Fórmula pra converter para Fahrenheit -> (t * 9/5) + 32
    ftemp_list = [(t * 9/5) + 32 for t in ctemps]
    ftemp_set = {(t * 9/5) + 32 for t in ctemps}
    print(ftemp_list)
    print(ftemp_set)
    # TODO: Crie um set a partir de uma string
    frase = "0 primeiro podcast Brasiliero sobre ciencia de dados"
    letras = {l.upper() for l in frase if not l.isspace()}
    print(letras)

if __name__ == "__main__":
    main()
