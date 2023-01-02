import numpy as np


def create_matriz(n):
    """Cria matriz de acordo com as linhas e colunas especificadas pelo usuário.

    Args: n (int): Número que irá ditar quantas linhas e colunas terá a matriz.
    """
    matriz = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f'Digite um número para sua matriz na posição [{i+1}, {j+1}]:'))
    return matriz


def determinante(n, matriz):
    """De acordo com a matriz criada, verifica o N e chama a função para calcular a determinante."""
    deter = 0
    if n == 2:
        deter = calcular_determinante_matriz_2x2(matriz)
    if n == 3:
        deter = calcular_determinante_matriz_3x3(matriz)
    if n == 4:
        deter = calcular_determinante_matriz_4x4(matriz)
    return deter


def calcular_determinante_matriz_2x2(matriz):
    """Recebe a matriz 2x2 e calcula sua determinante.

    Args:
        matriz: Matriz que será usada para calculara determinante.

    Return:
        deter: Determinante calculado a partir da matriz.
    """
    m = matriz
    deter = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return deter


def calcular_determinante_matriz_3x3(matriz):
    """Recebe a matriz 3x3 e calcula sua determinante.

    Args:
        matriz: Matriz que será usada para calculara determinante.

    Return:
        deter: Determinante calculado a partir da matriz.
    """
    m = matriz
    a = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]
    b = m[0][2] * m[1][1] * m[2][0] + m[0][1] * m[1][0] * m[2][2] + m[0][0] * m[1][2] * m[2][1]
    deter = a - b
    return deter


def calcular_determinante_matriz_4x4(matriz):
    """Recebe a matriz 4x4 e calcula sua determinante.

    Args:
        matriz: Matriz que será usada para calculara determinante.

    Return:
        deter: Determinante calculado a partir da matriz.
    """
    m = matriz
    matriz_retirada1 = np.zeros((3, 3))
    matriz_retirada2 = np.zeros((3, 3))
    matriz_retirada3 = np.zeros((3, 3))
    matriz_retirada4 = np.zeros((3, 3))

    for i in range(4):
        for j in range(4):
            if not i == 0 == j:
                matriz_retirada1[i-1][j-1] = matriz[i][j]

    for i in range(4):
        for j in range(4):
            if not i == 1 or j == 0:
                if 2 == i or i == 3:
                    matriz_retirada2[i - 1][j - 1] = matriz[i][j]
                else:
                    matriz_retirada2[i][j - 1] = matriz[i][j]

    for i in range(4):
        for j in range(4):
            if not i == 2 or j == 0:
                if i == 3:
                    matriz_retirada3[i-1][j-1] = matriz[i][j]
                else:
                    matriz_retirada3[i][j-1] = matriz[i][j]

    for i in range(3):
        for j in range(4):
            if not i == 3 or j == 0:
                matriz_retirada4[i][j-1] = matriz[i][j]
    # Retira as colunas e linhas da matriz para criar várias matrizes 3x3 e calcular sua determinante.
    deter_matriz_1 = calcular_determinante_matriz_3x3(matriz_retirada1)
    deter_matriz_2 = calcular_determinante_matriz_3x3(matriz_retirada2)
    deter_matriz_3 = calcular_determinante_matriz_3x3(matriz_retirada3)
    deter_matriz_4 = calcular_determinante_matriz_3x3(matriz_retirada4)
    # utiliza as determinantes das matrizes 3x3 que foi feito acima para calcular assim a 4x4
    deter1 = m[0][0] * ((-1)**(0+0) * deter_matriz_1) + m[1][0] * ((-1)**(1+0) * deter_matriz_2)
    deter2 = m[2][0] * ((-1)**(2+0) * deter_matriz_3) + m[3][0] * ((-1)**(3+0) * deter_matriz_4)
    deter = deter1 + deter2
    return deter


def matriz_inversa(matriz, n):
    """Faz um tratamento para saber se é possível calcular a inversa da matriz, caso seja, calcule e retorna o inverso
    da matriz.

    Args:
        matriz: a matriz que será usada para os cálculos.
        n: número de linhas e colunas da matriz.

    Return:
        matriz_identidade : essa variável se torna a matriz inversa no decorrer da função.
    """
    matriz_identidade = np.zeros((n, n))
    deter = 0
    if n == 2:
        deter = calcular_determinante_matriz_2x2(matriz)
    if n == 3:
        deter = calcular_determinante_matriz_3x3(matriz)
    if n == 4:
        deter = calcular_determinante_matriz_4x4(matriz)

    if deter == 0:
        a = 'Inversa não existe'
        return a
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    matriz_identidade[i][j] = 1

        for i in range(n):

            pivote = matriz[i][i]

            for k in range(n):
                matriz[i][k] = matriz[i][k] / pivote
                matriz_identidade[i][k] = matriz_identidade[i][k] / pivote

            for j in range(n):
                if i != j:
                    aux = matriz[j][i]

                    for k in range(n):
                        matriz[j][k] = matriz[j][k] - aux * matriz[i][k]
                        matriz_identidade[j][k] = matriz_identidade[j][k] - aux * matriz_identidade[i][k]
        return matriz_identidade


def mudanca_de_base():
    """A partir de 2 bases, cria uma matriz de mudança de base e printa."""
    n = int(input('Digite o número de elementos de sua base:'))
    a = np.zeros((n, n))
    b = np.zeros((n, n))

    for i in range(n):
        x = input(f'Digite os elementos para a base A na posição {i+1}:')
        x = x.split() # Retira os espaços para colocar os numeros na matriz da base
        x = np.asarray(x)
        for j in range(n):
            a[j][i] = x[j]

    for i in range(n):
        x = input(f'Digite os elementos para a base A na posição {i+1}:')
        x = x.split()
        x = np.asarray(x)
        for j in range(n):
            b[j][i] = x[j]
    b_inversa = matriz_inversa(b, n)
    matriz_a_base_b = np.dot(b_inversa, a)
    print(f'Matriz A na base B: \n {matriz_a_base_b}')
    matriz_b_base_a = matriz_inversa(matriz_a_base_b, n)

    print(f'Matriz B na base A: \n {matriz_b_base_a}')
