'''
Trabalhando com FOR LOOP dentro dos itens do dicionário.

'''

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': 'true'} # um dicionário é como uma lista, ele é mutavel.


# Vai imprimir SOMENTE AS KEYS, Sem os Values
print('Impressão SOMENTE DAS KEYS:')
for x in aluno:
    print(x)
print()

# Dessa forma também vai imprimir SOMENTE AS KEYS, Sem os Values
print('Forma 2 de imprimir SOMENTE AS KEYS,:')
for x in aluno.keys():
    print(x)

# Dessa forma imprimimos somente os VALUES, sem as Keys.
print('Impressão somente dos VALUES, sem as Keys:')
for x in aluno.values():
    print(x)
print()

# Essa forma irá imprimir as Keys com seus values em formato de tupla.
print('Keys + Values em formato de tupla:')
for x in aluno.items():
    print(x)
print()

# Desa forma ele tira os valores de dentro da tupla.
print('Keys + Values fora da tupla:')
for keys, values in aluno.items(): # (O nome das variaveis pode ser qualquer um, no exemplo usamos KEYS, VALUES)
    print(f'{keys}: {values}')     # Usei formated strings para ficar mais bonita e organizada a impressão.
print()

print(aluno)