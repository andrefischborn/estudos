'''
    Problema "baskara"
Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.
    Exemplo 1:
        Coeficiente a: 1
        Coeficiente b: 0
        Coeficiente c: -9
        X1 = 3.0000
        X2 = -3.0000
    Exemplo 2:
        Coeficiente a: 2
        Coeficiente b: -4.5
        Coeficiente c: 1.7
        X1 = 1.7697
        X2 = 0.4803
    Exemplo 3:
        Coeficiente a: 1
        Coeficiente b: 3
        Coeficiente c: 4
        Esta equacao nao possui raizes reais
'''

a = float(input('Qual o número do coeficiente A? '))
b = float(input('Qual o número do coeficiente B? '))
c = float(input('Qual o número do coeficiente C? '))

delta = (b ** 2) - 4 * a * c


if a == 0:
    print('O valor de a, deve ser diferente de 0')
elif delta < 0:
    print('Sem raízes reais')
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print((f'X1: %.4f' % (x1)),(f'X2: %.4f') % (x2))
