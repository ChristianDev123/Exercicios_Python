matriz_A = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]
somaA = 0
somaB = 0
somaC = 0
somaD = 0
for x in range(0, 4):
    for y in range(0, 4):
        numArray = int(input("Digite um valor para alocação na matriz A: "))
        matriz_A[x][y] = numArray
        #===========================================================
        
        # A
        '''
        XX--
        XX--
        ----
        ----
        '''
        if(x < 2 and y < 2):
            somaA += matriz_A[x][y]
        # =============================================================
        
        # B
        '''
        ----
        ----
        --xx
        --xx
        '''
        if(x > 1 and y > 1):
            somaB += matriz_A[x][y]
        # ==============================================================

        #C
        '''
        x---
        xx--
        xxx-
        xxxx
        '''
        if(x == 0):
            somaC += matriz_A[x][y]
        elif(x == 1 and y > 0):
            somaC += matriz_A[x][y]
        elif(x == 2 and y > 1):
            somaC += matriz_A[x][y]
        elif(x == 3 and y > 2):
            somaC += matriz_A[x][y]
        # ==============================================================

        #D
        '''
        -xxx
        --xx
        ---x
        ----
        '''
        if(x == 0 and y > 0):
            somaD += matriz_A[x][y]
        elif(x == 1 and y > 1):
            somaD += matriz_A[x][y]
        elif(x == 2 and y > 2):
            somaD += matriz_A[x][y]
print(somaA)
print(somaB)
print(somaC)
print(somaD)