# Usando funções transformadoras: sorted, filter, map


def primeiro_filtro(x):
    if x % 2 == 0:
        return False
    return True


def segundo_filtro(x):
    if x.isupper():
        return False
    return True


def quadrado(x):
    return x**2


def nota_para_conceito(x):
    if x >= 90:
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    # Definindo sequencias para usarmos nesta tarefa
    numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letras = "abcDeFGHiJklmnoP"
    notas = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: Use filter para remover itens de uma lista
    impares = list(filter(primeiro_filtro, numeros))
    # print(impares)
    # TODO: Use filter numa sequência de caracteres
    lower_case = list(filter(segundo_filtro, letras))
    #print(lower_case)
    # TODO: Use map para criar uma nova sequência de valores
    quadrados = list(map(quadrado, numeros))
    #print(quadrados)
    # TODO: Use sorted e map para mudar as noas para conceito
    notas = sorted(notas)
    conceitos = list(map(nota_para_conceito, notas))
    print(conceitos)
if __name__ == "__main__":
    main()
    
    
