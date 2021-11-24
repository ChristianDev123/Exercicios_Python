nota1 = int(input("Digite o primeiro valor das notas:"))
nota2 = int(input("Digite o segundo valor das notas:"))
nota3 = int(input("Digite o terceiro valor das notas:"))
nota4 = int(input("Digite o quarto valor das notas:"))
nota5 = int(input("Digite o quinto valor das notas:"))
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
print("A média é {}".format(media))

# FORMA MAIS INTEIGENTE
for i in range(5):
    nota = int(input("Digite sua {i}ª nota "))
    somaNota =  somaNota + nota
    i = i + 1
media = somaNota/5

print("A média é {media}")