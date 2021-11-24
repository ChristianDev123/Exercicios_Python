# Este programa será estático!
valorInicial = 2
valorFinal = 1
i = 0
while(valorInicial <= 9):
    while(i < 10):
        resultado = valorInicial * (i+1)
        print("{} * {} = {}".format(valorInicial,i+1,resultado))
        i = i + 1
    valorInicial = valorInicial + 1
    i = 0 