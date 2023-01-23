'''
Problema "soma_impares" (adaptado de URI 1071)
Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números
impares entre eles.

    Exemplo 1:
        Digite dois numeros:
        2
        9
        SOMA DOS IMPARES = 15
    Exemplo 2:
        Digite dois numeros:
        15
        10
        SOMA DOS IMPARES = 24
    Exemplo 3:
        Digite dois numeros:
        6
        -5
        SOMA DOS IMPARES = 5 
        '''
soma: int
print(f'Digite dois números:')
x = int(input())
y = int(input())

# Aqui realiza a troca entre as variaveis, caso o valor digitado para X ser maior que Y. Para não fica negativo:
if x > y:           
    troca = x       # o número que estava no X fica salvo na variável "troca"
    x = y           # Agora o número que estava no Y vai para o X
    y = troca       # E o Y recebe o número X que estava temporariamente na variável troca.

soma = 0 # A soma precisa começar do zero para não dar erro.

for i in range(x+1, y):
    if i % 2 != 0:          # Essa é a lógica para "se for impar". Se o resto do "I" for divisivel por 2 e diferente de zero, então:
        soma = soma + i     # 0 + i

print(f'A soma dos impares = {soma}')
