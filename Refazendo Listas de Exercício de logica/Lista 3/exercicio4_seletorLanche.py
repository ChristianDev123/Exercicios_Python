lanche = ["Big Mac", "Quarteirão", "McChicken", "Cheddar McMelt", "mcMax"]
respUsuario = int(input("Digite um código para escolher um lanche:\n [1] Big Mac\n [2] Quarteirão\n [3] McChicken\n [4] Cheddar McMelt\n [5] McMax\n"))
if(respUsuario == 1):
    codigo = 0
elif(respUsuario == 2):
    codigo = 1
elif(respUsuario == 3):
    codigo = 2
elif(respUsuario == 4):
    codigo = 3
elif(respUsuario == 5):
    codigo = 4
print("O lanche escolhido foi: {}".format(lanche[codigo]))