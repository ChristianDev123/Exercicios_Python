def primeira_funcao(fraseImpacto):
    print(fraseImpacto)


primeira_funcao("Forte Abraço Rapaziada!")
print("")

# ============================ calculadora ==================================
'''
numeros = []
resps = "s"


def soma(n1,n2):
    print(f"O resultado da soma é: {n1+n2}")


def subtracao(n1, n2):
    print(f"O resultado da subtracao é: {n1-n2}")


def multiplicacao(n1, n2):
    print(f"O resultado da multiplicação é: {n1*n2}")


def divisao(n1, n2):
    print(f"O resultado da divisão é: {n1/n2}")


while resps == "s":
    num1 = float(input(f"Digite o primeiro valor: "))
    num2 = float(input(f"Digite o segundo valor: "))
    numeros.append(num1)
    numeros.append(num2)
    print(numeros)
    operador = str(input("Selecione uma operação: \n[+] Adição \n[-] Subtração \n[*] Multiplicação \n[/] Divisão \n :"))
    if(operador == "+"):
        soma(numeros[0], numeros[1])
    elif(operador == "-"):
        subtracao(numeros[0], numeros[1])
    elif(operador == "*"):
        multiplicacao(numeros[0], numeros[1])
    elif(operador == "/"):
        divisao(numeros[0], numeros[1])

    resps = str(input("Digite 'n' para desligar o programa ou 's' para continuar a utiliza-lo: "))
'''
# ======================= Calculadora com return ====================================================
numeros = []
resps = "s"

def soma(n1,n2):
    somatoria = n1 + n2
    return somatoria

def subtracao(n1, n2):
    subs = n1 - n2
    return subs

def multiplicacao(n1, n2):
    produto = n1 * n2
    return produto

def divisao(n1, n2):
    divs = n1 / n2
    return divs

while resps == "s":
    numeros.clear()
    num1 = float(input(f"Digite o primeiro valor: "))
    num2 = float(input(f"Digite o segundo valor: "))
    numeros.append(num1)
    numeros.append(num2)
    
    operador = str(input("Selecione uma operação: \n[+] Adição \n[-] Subtração \n[*] Multiplicação \n[/] Divisão \n :"))
    if(operador == "+"):
        print(f"A soma dos elementos é: {soma(numeros[0],numeros[1])}")
    elif(operador == "-"):
        print(f"A subtração dos elementos é: {subtracao(numeros[0],numeros[1])}")
    elif(operador == "*"):
        print(f"A multiplicação entres os elementos é: {multiplicacao(numeros[0], numeros[1])}")
    elif(operador == "/"):
        print(f"A divisão entre os elementos é: {divisao(numeros[0], numeros[1])}")

    resps = str(input("Digite 'n' para desligar o programa ou 's' para continuar a utiliza-lo: "))
