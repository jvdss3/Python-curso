# Usando dict comprehensions


def main():
    # Definindo uma lista de temperaturas
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary
    # Dica: Fórmula pra converter para Fahrenheit -> (t * 9/5) + 32
    dicio_temp = {t: (t * 9/5) + 32 for t in ctemps if t < 100}
    print(dicio_temp)
    print(dicio_temp[12])
    
if __name__ == "__main__":
    main()
