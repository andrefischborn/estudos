'''
TRABALHANDO COM MULTIPLOS OPERADORES
'''

valor = input('Qual o valor? ')
valor = int(valor)

# forma longa:

if valor >= 20 and valor < 40:
    print('Produto aceito')
else:
    print('Produto não aceito')

# forma enxuta e organizada:

resultado = 'Produto Aceito' if 20 <= valor < 40 else 'Produto não aceito.'
print(f'{resultado} - Resultado da forma enxuta.')
