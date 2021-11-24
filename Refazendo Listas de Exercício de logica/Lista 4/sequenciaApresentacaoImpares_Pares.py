valor1 = int(input("Digite o primeiro valor da sequência: "))
valor2 = int(input("Digite o valor limite da sequência: "))
arrayValores = []
def posicionaValor(v1,v2):
    if(v1> v2):
        mem = v2
        v2 = v1
        v1 = mem
        print("houve um erro de digitação, o programa já resolveu!")
        arrayValores.append(v1)
        arrayValores.append(v2)
    else:
        print("Tudo Certo!")    
        arrayValores.append(v1)
        arrayValores.append(v2)

posicionaValor(valor1,valor2)
firstValor = int(arrayValores[0])
secondValor = int(arrayValores[1])

def calculo(val1,val2):
    valComp1 = val1
    valComp2 = val2
    print("sequência = [")
    while(val1 <= val2):
        print( "{},".format(val1))
        val1 = val1 + 1
    print("]")    
    while(valComp1 <= valComp2):
        if(valComp1 % 2 == 1):
            print("Impar:{}".format(valComp1))
        elif(valComp1 % 2 == 0):
            print("Par:{}".format(valComp1))
        valComp1 = valComp1 + 1

calculo(firstValor,secondValor)
    
        