'''
    Problema "dardo"
No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual
foi a maior.
    Exemplo 1:
        Digite as tres distancias:
        83.21
        79.53
        89.15
        MAIOR DISTANCIA = 89.15
    Exemplo 2:
        Digite as tres distancias:
        83.21
        87.20
        83.21
        MAIOR DISTANCIA = 87.20 
'''
dardo1 = float(input(f'Qual a distância do primeiro dardo? '))
dardo2 = float(input(f'Qual a distância do segundo dardo? '))
dardo3 = float(input(f'Qual a distância do terceiro dardo? '))

if (dardo1 > dardo2) and (dardo1 > dardo3):
    print(f'Maior distância: {dardo1} ')
elif (dardo2 > dardo3) and (dardo2 > dardo1):
    print(f'Maior distância: {dardo2} ')
else:
    print(f'Maior distância: {dardo3} ')
