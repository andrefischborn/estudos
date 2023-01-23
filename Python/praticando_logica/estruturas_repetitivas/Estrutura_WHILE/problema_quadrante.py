'''
        Problema "quadrante" (adaptado de URI 1115)
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no
sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence (Q1, Q2, Q3 ou Q4). O
algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem
escrever mensagem alguma).
    Exemplo:
        Digite os valores das coordenadas X e Y:
        2
        2
    QUADRANTE Q1
        Digite os valores das coordenadas X e Y:
        3
        -2
    QUADRANTE Q4
        Digite os valores das coordenadas X e Y:
        -8
        -1
    QUADRANTE Q3
        Digite os valores das coordenadas X e Y:
        -7
        1
    QUADRANTE Q2
        Digite os valores das coordenadas X e Y:
        0
        2
'''
print(f'Digite os valores das coordenadas X e Y:')
x = int(input())
y = int(input())

while x != 0 and y != 0:

    if x > 0 and y > 0:
        print(f'QUADRANTE Q1')

    elif x < 0 and y > 0:
        print(f'QUADRANTE Q2')

    elif x < 0 and y < 0:
        print(f'QUADRANTE Q3')
         
    else:
        print(f'QUADRANTE Q4')

    print(f'Digite os valores das coordenadas X e Y:')
    x = int(input())
    y = int(input())    
print('FIM')