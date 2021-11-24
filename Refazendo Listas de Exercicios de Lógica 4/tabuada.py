valorTabuada = int(input("Digite o número que você deseja saber a tabuada:\n"))

for i in range(10):
    resultado = valorTabuada * (i+1)
    print( "{} * {} = {}".format(valorTabuada, i+1, resultado))