'''
TRABALHANDO COM XARGS - ARGUMENTOS
'''

#criar uma função que soma vários números.

def soma(*numeros):
    return numeros


x = soma(2,3,4,5,6)     # Vai CONCATENAR, são strings!
print(f'A soma é: {x}')


# Forma correta de fazer:


def soma2(*numeros):
    resultado = 0   # Precisamos partir do zero(ponto de inicio), vamos somando: 0 + Argumento1 + Argumento2 + Argumento3... (0 +2 +3 +4...)
    for num in numeros:
        resultado += num    # A soma é realizada dentro do FOR LOOP.
    return resultado    # Aqui salvamos o resultado da primeira soma de argumento (0+2) que vai aguardar o próximo argumento (+3) e seguindo...


y = soma2(2,3,4,5,6)
print(f'A soma é: {y}')
