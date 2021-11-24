
def validaTriangulo(bu,au):
    if((bu == 0) or (au == 0)):
        print("Dados Inválidos!")
        return False
    else:
        return True

def validaEscolha(eu):
    if((eu == "s") or (eu == "n")):
        return True
    else:
        return False

def calculaAreaTriangulo():
    escolhaUsuario = str("s")
    while(escolhaUsuario == "s"):    
        baseUsuario = float(input("Insira a base do triângulo: "))
        alturaUsuario = float(input("Insira a altura do triângulo: "))
        if(validaTriangulo(baseUsuario,alturaUsuario) == False):
            print("Algum dos lados inseridos tem valor zero, o que invalida a existência de um triangulo, desligando o programa...")
            break
        elif(validaTriangulo(baseUsuario,alturaUsuario) == True):
            areaTriangulo = (baseUsuario * alturaUsuario)/2
            print("A area do triangulo é: {}".format(areaTriangulo))
            escolhaUsuario = str(input("Digite 's' para continuar no programa ou 'n' para paralizar o programa: "))
        if(validaEscolha(escolhaUsuario) == False):
            print("opção inserida está inválida, desligando o sistema...")
            break
        elif(validaEscolha(escolhaUsuario) == True):
            if(escolhaUsuario == "s"):
                escolhaUsuario = str("s")
                print("Você optou por se manter no programa...\n o programa está sendo reiniciado !")
            elif(escolhaUsuario == "n"):
                escolhaUsuario = str("n")
                print("Você escolheu sair do programa...\n O programa está sendo desligado !")
            print("=" * 50)
calculaAreaTriangulo()