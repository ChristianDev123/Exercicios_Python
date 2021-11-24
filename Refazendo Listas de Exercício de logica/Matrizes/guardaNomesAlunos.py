nomeAlunos = []
alunosPlus = "s"
while(alunosPlus == "s"):
    insereNome = str(input("Insira o nome do aluno: "))
    nomeAlunos.append(insereNome)
    continua = str(input("Deseja continuar no programa? \nDigite 's' para sim \nou 'n' para não\n:"))
    if(continua == "n"):
        print(f"Os nomes alocados foram: {nomeAlunos}")
        desejoRem = str(input("Deseja remover algum nome da lista? \n's' para sim e 'n' para não: "))
        if(desejoRem == "s"):
            respRemove = str(input("Digite a palavra que você deseja remover: "))    
            for i in range(len(nomeAlunos)):
                if(nomeAlunos[i] == respRemove):
                    nomeAlunos.pop(i)
            print(nomeAlunos)
            alunosPlus = "n"
        else:
            break