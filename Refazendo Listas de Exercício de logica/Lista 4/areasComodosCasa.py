guardaNomes = []
guardaAreas = []
plusComodo = "s"
areaCasa = 0
while(plusComodo == "s"):
    nomeComodo = str(input("Digite o nome do cômodo em questão: "))
    guardaNomes.append(nomeComodo)
    larguraComodo = float(input("Digite a largura do cômodo em m²: "))
    comprimentoComodo = float(input("Digite o comprimento do cômodo em m²:"))
    areaComodo = larguraComodo * comprimentoComodo
    guardaAreas.append(areaComodo)
    plusComodo = str(input("Tem mais algum comôdo a ser inserido no programa?\n's' para sim ou 'n' para não. \n:"))
    if(plusComodo == "s"):
        plusComodo = "s"
    elif(plusComodo == "n"):
        plusComodo = "n"
        controleFor = len(guardaNomes)
        for i in range(controleFor):
            print(f"O (a) {guardaNomes[i]} tem {guardaAreas[i]} m² de área!")
            areaCasa = areaCasa + guardaAreas[i]
        print(f"A área da casa é {areaCasa} m²")