salario = float(input("Digite seu salário (ainda sem aumento): "))
porcentagem = float(input("Digite a porcentagem de aumento: "))
novoSalario = (salario * (porcentagem/100)) + salario
print("O novo salário será: {}".format(novoSalario))
