matriz_D = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
for x in range(0,5):
    for y in range(0,5):
        valorArray = int(input("Aloque um valor inteiro na matriz: "))
        matriz_D[x][y] = valorArray
valorProcurado  = int(input("Digite o valor que deseja encontrar na matriz: "))
existe = 0
nExiste = 0
for x in range(0,5):
    for y in range(0,5):
        if(matriz_D[x][y] == valorProcurado):
           existe = int(valorProcurado)
           break 
        elif(matriz_D[x][y] != valorProcurado):
            nExiste = 3.14
if(existe == valorProcurado):
    print(f"O valor {valorProcurado} existe na matriz. O valor procurado está alocado na posição [{x},{y}] da matriz.")
elif(nExiste != valorProcurado):
    print(f"O valor {valorProcurado} não ecxiste na matriz!")
