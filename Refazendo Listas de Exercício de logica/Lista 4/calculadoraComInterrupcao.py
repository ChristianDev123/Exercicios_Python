continuar = "s"
while(continuar == "s"):
    num1 = float(input("Digite o primeiro valor: "))
    operador = str(input("Selecione a operação: \n[+] Adição \n[-] Subtração \n[*] Multiplicação \n[/] Divisão \n:"))
    num2 = float(input("Digite o segundo valor: "))
    if((num1 == 30000) or (num2 == 30000)):
        break
    else:
        if(operador == "+"):
           resultado = num1 + num2
        elif(operador == "-"):
           resultado = num1 - num2
        elif(operador == "*"):
           resultado = num1 * num2
        elif(operador == "/"):
           resultado = num1 / num2
        print(f"{num1} {operador} {num2} = {resultado}")
    continuar = str(input("Você deseja continuar no programa? \nDigite 's' para sim ou 'n' para não.  \n:"))