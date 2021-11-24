#FORMA MAIS SIMPLES:
idadeUsuario = int(input("Digite sua idade: "))
if(idadeUsuario <= 12):
    faixaEtaria = "Criança"
elif((idadeUsuario > 12) and (idadeUsuario <= 17)):
    faixaEtaria = "Adolescente"
elif((idadeUsuario > 17) and (idadeUsuario <= 59)):
    faixaEtaria = "Adulto"
elif(idadeUsuario > 59):
    faixaEtaria = "Idoso"
print("De acordo com a sua idade você se encaixa na faixa etária: {}".format(faixaEtaria))