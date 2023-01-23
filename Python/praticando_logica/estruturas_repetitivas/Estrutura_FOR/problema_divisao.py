'''
Problema "divisao" (adaptado de URI 1116)
Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.
    Exemplo:
    Quantos casos voce vai digitar? 3
    Entre com o numerador: 3
    Entre com o denominador: -2
    DIVISAO = -1.50

    Entre com o numerador: -8
    Entre com o denominador: 0
    DIVISAO IMPOSSIVEL

    Entre com o numerador: 0
    Entre com o denominador: 8
    DIVISAO = 0.00 
'''
quantidade = int(input('Quantos casos você vai digitar? '))

for i in range (0, quantidade):
        numerador = float(input('Digite o númerador: '))
        denominador = float(input('Digite o númerador: '))
        if denominador == 0:
            print(f'DIVISÃO IMPOSSÍVEL')
        else:
            calculo = numerador / denominador
            print(f'DIVISÃO = {calculo:.4f}')