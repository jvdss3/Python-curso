# Personalizando representações string de classes


class Pessoa():
    def __init__(self):
        self.nome = "Jessica"
        self.sobrenome = "Temporal"
        self.idade = 25

    # TODO: Use __repr__ para criar uma string que seja útil para debug
    def __repr__(self):
        dados1 = [self.nome, self.sobrenome, self.idade]
        texto = "<Classe Pessoa- nome: {0}, sobrenome: {1}, idade: {2}>"
        return texto.format(self.nome, self.sobrenome, self.idade)
    # TODO: Use __str__ para criar uma string amigável para humanos
    def __str__(self):
        texto = "Pessoa {0} {1} tem {2} anos"
        return texto.format(self.nome, self.sobrenome, self.idade)
    
    # TODO: Use bytes para converter a string em um objeto bytes
    def __bytes__(self):
        dados = [self.nome, self.sobrenome, self.idade]
        para_bytes = "Pessoa: {0}: {1}:{2}".format(*dados)
        return para_bytes.encode('utf-8')

def main():
    # Criando uma instância de Pessoa
    pessoa = Pessoa()

    # Usando as funções embutidas de Python para representar a pessoa
    # numa string
    print(repr(pessoa))
    print(str(pessoa))
    print("Formatado: {0}".format(pessoa))
    print(bytes(pessoa))

if __name__ == "__main__":
    main()
