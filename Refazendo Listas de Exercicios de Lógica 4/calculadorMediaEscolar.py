alunosRep = 0
alunosExame = 0
alunosApr = 0
mediaClasse = 0
for aluno  in range(1,7):
    notaUsuario1 = float(input("Insira a primeira nota do aluno {}: ".format(aluno)))
    notaUsuario2 = float(input("Insira a segunda nota do aluno {}: ".format(aluno)))
    media = (notaUsuario1 + notaUsuario2)/2
    if(media < 3):
        classificacao = "Reprovado"
        alunosRep = alunosRep + 1
    elif((media >= 4) and (media < 7)):
        classificacao = "Exame"
        alunosExame = alunosExame + 1
    elif(media >=7):
        classificacao = "Aprovado"
        alunosApr = alunosApr + 1
    mediaClasse = mediaClasse + media
    print("A média deste aluno, em específico, é: {}".format(media))    
    print("Alunos Aprovados: {}".format(alunosApr))
    print("Alunos Exame: {}".format(alunosExame))
    print("Alunos Reprovados: {}".format(alunosRep))
    print("Media da Classe: {}".format(mediaClasse))
    print("="*50)
    