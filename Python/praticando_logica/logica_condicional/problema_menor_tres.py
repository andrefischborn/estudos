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
a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))

if a < b and a < c:
    menor = a
elif b < c and b < c:
    menor = b
elif a == b == c:
    menor = f'Nenhum, são todos iguais: {a}'
else:
    menor = c


print(f'O menor número entre {a}, {b} e {c} é:')
print(f' O menor número é: {menor}.')
