while True:
    nota=int(input('Insira a nota do aluno: '))
    if nota>=10 and nota<=0:
        print('Nota invalida!')
    if nota<10 and nota>0:
        break
    
print('Nota Inserida.')