'''
    Problema "media_idades"
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
mostrar a mensagem "IMPOSSIVEL CALCULAR".
    Exemplo 1:
        Digite as idades:
        31
        27
        46
        -5
        MEDIA = 34.67
    Exemplo 2:
        Digite as idades:
        -10
        IMPOSSIVEL CALCULAR 
'''
print('Digite as idades: ')
idades = int(input())
soma = 0
cont = 0

while idades >= 0:
    soma = soma + idades  
    cont = cont + 1
    print('Digite outra idade: ')
    idades = int(input())

if cont == 0:
    print(f'IMPOSSÍVEL CALCULAR.')
else:
    media = soma / cont
    print(f'MÉDIA: {media:.2f}')   



