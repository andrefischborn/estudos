'''
        Problema "multiplos" (adaptado de URI 1044)
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os
números podem ser digitados em qualquer ordem.
    Exemplo 1:
        Digite dois numeros inteiros:
        6
        24
        Sao multiplos
    Exemplo 2:
        Digite dois numeros inteiros:
        24
        6
    Sao multiplos
        Exemplo 3:
    Digite dois numeros inteiros:
        13
        5
    Nao sao multiplos 

    #Dica: Para saber se o número é multiplo, você precisa dividir o maior pelo menor e o resto tem que ser zero.
'''
x = int(input('Qual o valor do primeiro número? '))
y = int(input('Qual o valor do segundo número? '))

if (x % y == 0) or (y % x == 0):
    print (f'São multiplos!')
else:
    print(f'Não são multiplos!')
