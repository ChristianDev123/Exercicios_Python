base = int(input("Insira o valor da base da potenciação: "))
expoente = int(input("Insira o valor do expoente da potenciação: "))
res = base**expoente
expoente -= 1
print("")
while(expoente > 0):
    print(f"{base}\n *")
    expoente -= 1
print(f"{base}\n= \n{res}")
    