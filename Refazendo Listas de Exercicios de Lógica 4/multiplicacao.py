num1 = int(input("Insira o valor da base da potenciação: "))
num2 = int(input("Insira o valor do expoente da potenciação: "))
res = num1 * num2
num2 -= 1
print("")
while(num2 > 0):
    print(f"{num1}\n +")
    num2 -= 1
print(f"{num1}\n= \n{res}")
