import matrizes


def main():
    n = int(input('Digite o número de linhas e colunas da sua matriz:'))
    matriz = matrizes.create_matriz(n)
    print(f'Matriz: \n {matriz}')
    print('-'*30)
    deter = matrizes.determinante(n, matriz)
    print(f'Determinante da matriz: {deter}')
    inversa = matrizes.matriz_inversa(matriz, n)
    print('-'*30)
    print(f'Matriz inversa: \n {inversa}')
    matrizes.mudanca_de_base()


main()
