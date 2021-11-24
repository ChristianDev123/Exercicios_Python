qtdPes = float(input("Digite a quantidade de pés para a conversão"))
# conversão para polegadas
qtdPolegadas = qtdPes * 12
# conversão para jardas
qtdJardas = qtdPes / 3
# conversão para milhas
qtdMilhas = (qtdPes/3)/1760
print("Pés - Polegadas: {}".format(qtdPolegadas))
print("Pés - Jardas: {}".format(qtdJardas))
print("Pés - Milhas: {}".format(qtdMilhas))
