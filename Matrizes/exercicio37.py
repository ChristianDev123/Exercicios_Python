matriz_Resps = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0]
]
matriz_RespsUsuario = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
array_G = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
pontuacao = 0
for i in range(0,len(array_G)):
    respsUsuario = int(input(f"Digite o placar do {i+1}º jogo :"))
    if((respsUsuario == 1) or(respsUsuario == 2) or (respsUsuario == 3)):
        array_G[i] = respsUsuario
    else:
        print("[Error], Há um animal apostando!")
        break

for x in range(0, len(matriz_RespsUsuario)):
    respostaUsuario = array_G[x]
    for y in range(0,len(matriz_RespsUsuario[0])):
        matriz_RespsUsuario[x][respostaUsuario - 1] = 1
print(f"Aposta do Usuário: {matriz_RespsUsuario}")

for x in range(0,len(matriz_Resps)):
    for y in range(0, len(matriz_Resps[0])):
        if((matriz_Resps[x][y] == 1) and (matriz_RespsUsuario[x][y] == 1)):
            pontuacao += 1
print(f"Pontuação do Usuário: {pontuacao}")
print(f"Respostas certas: {matriz_Resps}")