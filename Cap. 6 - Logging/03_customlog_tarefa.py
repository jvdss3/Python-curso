# Personalizando o retorno do logging
import logging


# TODO: Crie uma outra função para rodar o log
dados = {"pessoas":"Joao"}

def main():
    # TODO: Defina o nível de log para debug e um arquivo para salvar
    def outra_funcao():
        logging.info("Esta é uma mensagem de informação", extra=dados)
    # o retorno. Use também uma formatação personalizada
    formato = "%(asctime)s: %(levelname)s: %(funcName)s: Pessoas:%(pessoas)s"

    logging.basicConfig(filename="output.log", level=logging.DEBUG, format=formato)


    logging.info("Esta é uma mensagem de informação", extra=dados)
    logging.warning("Esta é uma mensagem de aviso", extra=dados)
    outra_funcao()

if __name__ == "__main__":
    main()  
