'''
Problema "media_ponderada" (adaptado de URI 1079)
Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
pela soma dos pesos.
    Exemplo:
    Quantos casos voce vai digitar? 3
    Digite tres numeros:
        6.5
        4.3
        6.2
        MEDIA = 5.7
    Digite tres numeros:
        5.1
        4.2
        8.1
        MEDIA = 6.3
    Digite tres numeros:
        8.0
        9.0
        10.0
        MEDIA = 9.3 
'''
media = 0
N = int(input('Quantos casos voce vai digitar? '))

for casos in range(0, N):
    print(f'Digite {N} numeros: ')
    a = float(input())
    b = float(input())
    c = float(input())
    media = (a * 2 + b * 3 + c * 5) / 10
    print(f'MÉDIA = {media:.1f}')