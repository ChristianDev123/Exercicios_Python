matriz_G = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
sL = [0, 0, 0, 0, 0]
sC = [0, 0, 0, 0, 0]
somaColunasZero = 0
somaColunasUm = 0
somaColunasDois = 0
somaColunasTres = 0
somaColunasQuatro = 0

for x in range(0, 5):
    for y in range(0, 5):
        matriz_G[x][y] = int(input("Digite um valor a ser alocado na matriz: "))
        if(y == 0):
            somaColunasZero += matriz_G[x][y] 
            sC[0] = somaColunasZero
        elif(y == 1):
            somaColunasUm += matriz_G[x][y] 
            sC[1] = somaColunasUm
        elif(y == 2):
            somaColunasDois += matriz_G[x][y]
            sC[2] = somaColunasDois
        elif(y == 3):
            somaColunasTres += matriz_G[x][y]
            sC[3] = somaColunasTres
        elif(y == 4):
            somaColunasQuatro += matriz_G[x][y]
            sC[4] = somaColunasQuatro
    somaLinhas = sum(matriz_G[x])
    sL[x] = somaLinhas
print(matriz_G)
print(f"Soma Linha: {sL}")
print(f"Soma Coluna: {sC}")
