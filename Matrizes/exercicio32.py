matriz_A = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0], 
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
matriz_B = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0], 
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
matriz_S = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0], 
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]
matriz_D = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0], 
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]

for x in range(0,4):
    for y in range(0,6):
        matriz_A[x][y] = int(input("Digite um valor a ser alocado na matriz A: "))
        matriz_B[x][y] = int(input("Digite um valor a ser alocado na matriz B: "))
        elementoA = matriz_A[x][y]
        elementoB = matriz_B[x][y]
        somaAB = elementoA + elementoB
        diferencaAB = elementoA - elementoB
        matriz_S[x][y] = somaAB
        matriz_D[x][y] = diferencaAB
print(f"matriz A:\n {matriz_A}")
print(f"matriz B:\n {matriz_B}")
print(f"matriz soma de A-B:\n {matriz_S}")
print(f"matriz diferença de A-B:\n {matriz_D}")