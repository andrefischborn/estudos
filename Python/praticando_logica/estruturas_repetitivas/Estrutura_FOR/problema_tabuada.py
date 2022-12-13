'''
        Problema "tabuada"
Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.
Exemplo:
    Deseja a tabuada para qual valor? 4
        4 x 1 = 4
        4 x 2 = 8
        4 x 3 = 12
        4 x 4 = 16
        4 x 5 = 20
        4 x 6 = 24
        4 x 7 = 28
        4 x 8 = 32
        4 x 9 = 36
        4 x 10 = 40 
'''
fator = int(input('Deseja a tabuada para qual valor? '))

for fator_fixo in range(1, 11):
    produto = fator * fator_fixo    # A ordem dos fatores não altera o produto. ;)
    print(f'{fator_fixo} x {fator} = {produto}')
