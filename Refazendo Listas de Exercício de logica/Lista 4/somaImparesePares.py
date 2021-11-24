somaPar = 0
somaImpar = 0
maxNum = 10
for i in range(maxNum):
    numUsuario = int(input("Insire um valor: "))
    if(numUsuario % 2 == 0):
        somaPar = somaPar + numUsuario
       
    elif(numUsuario%2 == 1):
        somaImpar = somaImpar + numUsuario        
print("Par: {}".format(somaPar))
print("Impar: {}".format(somaImpar))        
print("=" * 40)