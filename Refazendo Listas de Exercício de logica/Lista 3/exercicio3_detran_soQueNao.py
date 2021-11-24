velocidadeVia = int(input("Digite a velocidade máxima da via: "))
velocidadeMotorista = float(input("Digite a velocidade em que estava no momento da infração: "))
diferencaDeVelocidade = velocidadeMotorista - velocidadeVia
if(diferencaDeVelocidade > 1):
    if(diferencaDeVelocidade <= 10):
        multaAPagar = 50
    elif((diferencaDeVelocidade > 10) and (diferencaDeVelocidade <= 30)):
        multaAPagar = 100
    elif(diferencaDeVelocidade > 30):
        multaAPagar = 200
    print("De acordo com a sua velocidade o valor da multa é: {}".format(multaAPagar))
else:
    print("Não houve infração, PARABENS!!!")
