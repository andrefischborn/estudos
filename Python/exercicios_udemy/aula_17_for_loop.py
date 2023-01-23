'''
CRIANDO UM CONJUNTO DE CARACTERES EM FORMA DE QUADRADO 6X6
USADO FOR LOOP

'''
linhas = 6
colunas = 6
simbolo = "O"

for l in range(linhas):
    for c in range(colunas):
        print(f'{simbolo}',end=' ')
    print()
