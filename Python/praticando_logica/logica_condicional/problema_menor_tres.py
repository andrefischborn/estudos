'''
        Problema "menor_de_tres"
Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
números lidos. Em caso de empate, mostrar apenas uma vez.
    Exemplo 1:
        Primeiro valor: 7
        Segundo valor: 3
        Terceiro valor: 8
        MENOR = 3
    Exemplo 2:
        Primeiro valor: 5
        Segundo valor: 12
        Terceiro valor: 5
        MENOR = 5
    Exemplo 3:
        Primeiro valor: 9
        Segundo valor: 9
        Terceiro valor: 9
        MENOR = 9 
'''
num1 = int(input('Qual o primeiro número? '))
num2 = int(input('Qual o segundo número? '))
num3 = int(input('Qual o terceiro número? '))

if (num1 <= num2) and (num1 <= num3):
    menor = num1
elif (num2 <= num3) and (num2 <= num3):
    menor = num2
else:
    menor = num3


print(f'O menor número entre {num1}, {num2} e {num3} é:')
print(menor)
