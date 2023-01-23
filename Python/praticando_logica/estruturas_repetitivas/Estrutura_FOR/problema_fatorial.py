'''
Problema "fatorial" (adaptado de URI 1153)
Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
fatorial de N.

    Exemplo 1:
        Digite o valor de N: 4
        FATORIAL = 24
    Exemplo 2:
        Digite o valor de N: 0
        FATORIAL = 1
    Exemplo 3:
        Digite o valor de N: 6
        FATORIAL = 720
    Exemplo 4:
        Digite o valor de N: 1
        FATORIAL = 1

'''

N = int(input(f'Digite o valor de N: '))
fat = 1

if N > 15:
    print(f'Erro, digite um número menor que 15!')
else:
    for i in range(1, N+1):
        fat = fat * i
    print(f'O Fatorial de {N}: {fat}')
