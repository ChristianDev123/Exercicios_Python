
while(True):
    valorUsuario = str(input("Insira um valor: "))
    ordem = str(input("Insira a ordem que deseja que seja apresentada: "))
    def crescenteDecrescente(num):
        novoArrayCrescente = []
        len(novoArrayCrescente) = len(num)
        maiorNum = 0
        menorNum = 0
        #crescente
        for i in range(len(num)):
            if(i>0):
                if(num[i-1] < num[i]):
                    
                if(num[i-1] > num[i]):

    def reverso(num):
        x = 0
        novoArray = []
        indice = len(num)
        for i in range(0,len(num)):
            novoArray.append(num[indice-1])
            x += 1
            indice -= 1
        return novoArray  
    print(crescenteDecrescente(valorUsuario))
    print(reverso(valorUsuario))
    continuar = str(input("Deseja continuar? \n[s] para sim \n[n] para não \n:"))
    if(continuar == "n"):
        break