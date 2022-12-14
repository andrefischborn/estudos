'''
Problema "sequencia_impares" (adaptado de URI 1067)
Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
se for o caso.
    Exemplo:
        Digite o valor de X: 8
        1
        3
        5
        7 
'''
x = int(input(f'Qual o valor de "X"? '))

for i in range(1, x):
    if i % 2 != 0:
        print(i)
if x % 2 != 0:
    print(x)