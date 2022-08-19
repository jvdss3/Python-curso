# Usando funções iteradoras como enumerate, zip, iter, next


import enum


def main():
    # Defina a lista de dias da semana em Português e English
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # TODO: Use a função iter para criar um iterador sobre uma lista
    iterador_dias = iter(dias)
    print(next(iterador_dias))
    print(next(iterador_dias))
    print(next(iterador_dias))
    # TODO: Use uma função para iterar sobre um arquivo
    # with open('dados.txt', 'r') as fp:
    #     for linha in iter(fp.readline, ''):
    #         print(linha)

    # TODO: Use a iteração tradicional (range) sobre a lista dias
    # for numero in range(len(dias)):
    #     print(numero, dias[numero])
    # TODO: Usar a função enumerate reduz a quantidade de código e te
    # dá um contador
    # for i, dia in enumerate(dias):
    #     print(i, dia)
    # TODO: Use a função zip para combinar as listas
    # for d in zip(dias, dias_en):
    #     print(d)

    # TODO: Combine zip com enumerate para formatar o resultado
    for i, d in enumerate(zip(dias, dias_en)):
        print(i,d[0], "=", d[1], "em Inglês")

if __name__ == "__main__":
    main()
