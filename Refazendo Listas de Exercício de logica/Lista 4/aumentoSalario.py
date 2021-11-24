salarioInicial = float(input("Insira seu primeiro salário: "))
percentAumentoAno2 = float(input("Insira a porcentagem do primeiro aumento de salário: "))
anoInicial = int(input("Insira o ano incial do contrato: "))
anoFinal = int(input("Insira o atual ano: "))
salarioAno2 = (salarioInicial * (percentAumentoAno2/100)) + salarioInicial


while(anoInicial <= anoFinal):
    percentAumentoNovo = percentAumentoAno2 * 2
    novoSalario = (salarioAno2 * (percentAumentoNovo/100)) + salarioAno2
    print(f"No ano de {anoInicial} o salário foi {round(novoSalario,2)}")
    salarioAno2 = novoSalario
    percentAumentoAno2 = percentAumentoNovo
    anoInicial = anoInicial + 1