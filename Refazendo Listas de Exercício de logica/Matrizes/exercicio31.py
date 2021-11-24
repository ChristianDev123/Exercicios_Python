
matriz_exe31 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
somaTudo = 0
somaDiagonalPrincipal = 0
somaColuna3 = 0
somaDiagonalSecundaria = 0
for x in range(0,5):
    for y in range(0,5):
        matriz_exe31[x][y] = int(input("Digite um número: "))
        somaTudo += matriz_exe31[x][y]
        print(matriz_exe31)
        if(x == 2):
            somaLinha3 = sum(matriz_exe31[x])
        if(y == 2):
            somaColuna3 += matriz_exe31[x][y]
        if(x==y):
            somaDiagonalPrincipal += matriz_exe31[x][y]
        if(((x==0)and(y==4))or((x==1)and(y==3))or((x==2)and(y==2))or((x==3)and(y==1))or((x==4)and(y==0))):
            somaDiagonalSecundaria += matriz_exe31[x][y]

print(somaLinha3)
print(somaColuna3)
print(somaDiagonalPrincipal)
print(somaDiagonalSecundaria)
print(somaTudo)



'''
somaLinha3 = 0
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for linhas in range(0,3):
    for colunas in range(0,3):
        matriz[linhas][colunas] = int(input("digite um valor: "))
        print(matriz)
        if(linhas == 2):
            somaLinha3 = sum(matriz[linhas])
print(somaLinha3)
'''