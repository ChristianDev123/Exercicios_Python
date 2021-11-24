nomesMeses = [
    "Janeiro",
    "Fevereiro",
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro',
]
continua = "s"
while(continua == "s"):
    numMes = int(input("Digite um número que equivale a um mês para recebe-lo por extenso: "))
    numMes -= 1
    print(f"O mês em questão é: {nomesMeses[numMes]}")
    loop = str(input("Digite 's' para continuar no programa \nou 'n' para desligar o sistema: "))
    if(loop == "n"):
        print("O programa está sendo desligado...")
        continua = "n"
    