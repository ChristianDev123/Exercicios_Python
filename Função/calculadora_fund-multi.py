res = 0
continuar = "s"
while(continuar == "s"):
    operador = str(input("Selecione uma operação: \n[+]Adição \n[-]Subtração \n[*]Multiplicação \n[/]Divisão \n:"))
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    def adicao(n1,n2):
        return n1 + n2
    def subtracao(n1,n2):
        return n1 - n2
    def multiplicacao(n1,n2):
        for i in range(0, n2-1):
            n1 = adicao(n1,n1)
        return n1
    def divisao(n1,n2):
        return n1 / n2
    if(operador == "+"):
        print(f"O resultado da soma é: {adicao(num1,num2)}")
    elif(operador == "-"):
        print(f"O resultado da subtração é: {subtracao(num1,num2)}")
    elif(operador == "*"):
        print(f"O resultado da multiplicação é: {multiplicacao(num1,num2)}")
    elif(operador == "/"):
        print(f"O resultado da divisão é: {divisao(num1,num2)}")
    continuar = str(input("Digite 's' para continuar no programa ou \ndigite 'n' para sair do programa \n:"))