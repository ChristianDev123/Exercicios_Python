somaIdadeOtimo = 0
otimo = 0
bom = 0
regular = 0
for i in range(1,16):
    opiniaoUsuario = int(input("Digite sua nota para o filme: \n3 - Ótimo \n2-Bom \n1-Regular\n "))
    idadeUsuario = int(input("Digite sua Idade: "))
    if(opiniaoUsuario == 1):
        otimo += 1
        somaIdadeOtimo += idadeUsuario
        mediaIdadeOtimo = somaIdadeOtimo/otimo
    elif(opiniaoUsuario == 2):
        bom += 1
        percentBom = bom/i
    elif(opiniaoUsuario == 3):
        regular += 1
print("A média de idade de quem respondeu bom é: {}".format(mediaIdadeOtimo))
print("O percentual de pessoas que respondeu Bom é:{}".format(percentBom*100))
print("A quantidade de Pessoas que respondeu regular é: {}".format(regular))
