lado1 = float(input("Insira o primeiro lado do triangulo: "))
lado2 = float(input("Insira o segundo lado do triangulo: "))
lado3 = float(input("Insira o terceiro lado do triangulo: "))

def validaTriangulo(lado1, lado2, lado3):
    if((lado1 == 0) or (lado2 == 0) or (lado3 == 0)):
        return False
    elif((lado1 > lado2+lado3) or (lado2 > lado1+lado3) or (lado3 > lado1+lado2)):
        return False
    else:
        return True

def calcula():
    if(validaTriangulo(lado1, lado2, lado3) == False):
        print("Este triangulo é impossível de existir!")
    else:
        if(lado1 == lado2 and lado1 == lado3):
            classificacao = "Equilátero"
        elif((lado1 != lado2 and lado1 == lado3) or (lado2 != lado3 and lado2 == lado1) or (lado3 != lado1 and lado3 == lado2)):
            classificacao = "Isósceles"
        elif((lado1 != lado2) and (lado1 != lado3)):
            classificacao = "Escaleno"
        print("Os valores inseridos formam um triangulo {}".format(classificacao))

calcula()