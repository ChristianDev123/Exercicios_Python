percurso = 2500
passosEfetivos = 0
passosDados = 0
medidaPasso = 0.47

while(percurso > 0):
    percurso -= medidaPasso
    passosEfetivos += 1
    passosDados += 1
    if(passosDados == 10):
        percurso += medidaPasso
        passosDados = 0
    res = passosEfetivos
print(f" o montanhista precisa de {res} passos para alcançar o topo da mintanha")