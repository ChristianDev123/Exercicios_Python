primeiroTermo = 1
segundoTermo = 1
termoAnt = 0
proxTermo = 0
qtdLoop = int(input("Insira a posição que deseja saber da sequência de Fibonacci:  "))
qtdLoop -= 1
print(primeiroTermo)
print(segundoTermo)
for i in range(1,qtdLoop):
    if(i == 1):
        proxTermo = primeiroTermo + segundoTermo
        termoAnt = proxTermo
    elif(i == 2):
        segundoTermo = termoAnt
        proxTermo = segundoTermo + primeiroTermo
        termoAnt = proxTermo
    elif((i != 1) or (i != 2)):
        primeiroTermo = segundoTermo
        segundoTermo = termoAnt
        proxTermo = segundoTermo + primeiroTermo
        termoAnt = proxTermo
    print(proxTermo)
