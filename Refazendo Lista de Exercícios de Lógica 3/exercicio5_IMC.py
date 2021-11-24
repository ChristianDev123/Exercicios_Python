classificacao = [
    "Magreza",
    "Saudável",
    "Sobrepeso",
    "Obesidade",
]
peso = float(input("Insira sua massa corporal: "))
altura = float(input("Insira a sua altura em metros: "))
imc = peso / (altura**2)
if(imc < 18):
    nivel = 0
elif(imc >=18 and imc < 25):
    nivel = 1
elif(imc >= 25 and imc < 30):
    nivel = 2
elif(imc >= 30):
    nivel = 3
print("A sua classificação é : {}".format(classificacao[nivel]))