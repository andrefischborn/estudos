'''
A estrutura repetitiva "PARA" - "FOR", é uma estrutura de controle que repete um bloco de comandos
para um certo intervalo de valores.
----------------------------------------------------------------------------------------------------------------------------
---- QUANDO USAR: Quando se sabe previamente a quantidade de repetições ou o intervalo de valores. -------------------------
----------------------------------------------------------------------------------------------------------------------------
Exemplo:
    Fazer um programa que Lê um valor inteiro "N" e depois N números inteiros. No final mostra a soma dos "N" números lidos.
    Quantos números serão digitados?  3
    Digite um número: 5              #1
    Digite um número: 2              #2
    Digite um número: 4              #3
    SOMA = 11
'''

N = int(input(f'Quantos números serão digitados? '))
soma = 0
for i in range(0, N):
    num1 = int(input(f'Digite um número: '))
    soma = soma + num1
print(f'SOMA: {soma}')
