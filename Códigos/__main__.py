import sys
from my_structure import HashTable


def process_file(input_file, output_file):
    """
    Função que processa um arquivo de entrada contendo números inteiros e
    escreve um arquivo de saída indicando se cada número é inédito ou repetido.
    """
    hash_table = HashTable()

    with open(input_file, "r") as entrada, open(output_file, "w") as saida:
        for linha in entrada:
            numero = int(linha.strip())

            if hash_table.contains(numero):
                saida.write(f"{numero} repetido\n")
            else:
                hash_table.insert(numero)
                saida.write(f"{numero} inedito\n")

    print("Números armazenados:", hash_table.get_numbers())


if __name__ == "__main__":
    """
    Ponto de entrada do programa. Verifica se os argumentos estão corretos e
    chama a função process_file com os arquivos especificados.
    """
    if len(sys.argv) != 3:
        print("Uso: python __main__.py <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(
        input_file, output_file
    )  # Chama a função principal passando os arquivos
