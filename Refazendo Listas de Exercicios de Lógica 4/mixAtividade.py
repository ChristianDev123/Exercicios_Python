i = 0
guardaNum = []
def calculo():
    somaNum = 0
    somaPar = 0
    qtdImpar = 0
    mediaPar = 0
    for i in range(1,11):
        numUsuario = float(input("Insira um valor: "))
        if(numUsuario == 30000):
            print("Você digitou 30.000, o programa está sendo desligado...")
            break
        guardaNum.append(numUsuario)
        somaNum = somaNum + numUsuario
        mediaNum = somaNum/i
        print("Média de todos os números: {}".format(mediaNum))
        print("Maior número: {}".format(max(guardaNum)))
        print("Menor número: {}".format(min(guardaNum)))
        if(identificaPar_Impar(numUsuario) == "par"):
            somaPar = somaPar + numUsuario
        elif(identificaPar_Impar(numUsuario) == "impar"):
            qtdImpar = qtdImpar + 1
        mediaPar = somaPar / i
        porcentImpar = (qtdImpar / i) * 100
        print("Media dos números pares:{} ".format(mediaPar))
        print("Porcentagem dos números impares:{} %".format(porcentImpar))
        print("=" * 50)

def identificaPar_Impar(numU):
    if(numU % 2 == 0):
        return "par"
    elif(numU % 2 == 1):
        return "impar"

calculo()