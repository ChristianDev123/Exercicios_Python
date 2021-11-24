ocupacoes = ["Matemático", "Analista de Sistemas", "Físico", "Arquiteto", "Piloto de Aeronaves"]
codigoProfissao = int(input("Digite 1 para Matemático\n Digite 2 para Analista de Sistemas\n Digite 3 para Físico\n Digite 4 para Arquiteto\n Digite 5 para Piloto de Aeronaves\n"))
print("A ocupação de fulano é {}".format(ocupacoes[codigoProfissao-1]))