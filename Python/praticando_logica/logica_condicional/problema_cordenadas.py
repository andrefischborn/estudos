'''
Problema "coordenadas" (adaptado de URI 1041)
Leia os valores das coordenadas X e Y de um ponto no plano
cartesiano. A seguir, determine qual o quadrante ao qual pertence o
ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a
mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva
“Eixo X” ou “Eixo Y”, conforme for a situação. 
                                                        y
                                                    Q2  |   Q1
                                                x   ---------- 
                                                    Q3  |   Q4
    Exemplo 1:
        Valor de X: 4.5
        Valor de Y: -2.2
        Q4
    Exemplo 2:
        Valor de X: 3.1
        Valor de Y: 2.0
        Q1
    Exemplo 3:
        Valor de X: 0
        Valor de Y: 0
        Origem
    Exemplo 4:
        Valor de X: 3.8
        Valor de Y: 0
        Eixo X
'''
print(f'Digite o valor de X e Y:')
x = float(input())
y = float(input())

if x == 0 and y == 0:
    print('Origem')
if x > 0 and y > 0:
    print(f'Q1')
if x < 0 and y > 0:
    print(f'Q2')
if x < 0 and y < 0:
    print(f'Q3')
if x > 0 and y < 0:
    print(f'Q4')
if x == 0:
    print('EIXO Y')
if y == 0:
    print('EIXO X')