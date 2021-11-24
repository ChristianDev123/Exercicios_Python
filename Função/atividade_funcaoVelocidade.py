def divisao(distancia,tempo):
    velMed = distancia/tempo
    return velMed 
def velocidadeMedia(d,t):
    return divisao(d,t)

dist = float(input("Insira a distância percorrida em metros: "))
temp = float(input("Insira o tempo utilizado em segundos: "))
print(f"A velocidade média em m/s é: {velocidadeMedia(dist,temp)} ")