'''
Usando Lista dentro de dicionários:
Observamos na Key "materias"
'''

# Variaveis que contém muitos dados, como os dicionarios, podemos organizar dessa forma:
aluno = {
    'nome': 'Ana', 
    'idade': 16, 
    'nota_final': 'A', 
    'aprovacao': 'true', 
    'materias': ['Física', 'Matemática', 'Inglês']
}
# O código fica mais organizado visivelmente.

print(aluno)
print()

# Aqui imprimimos a Key que contém uma lista interna:
print(aluno['materias'])

# Outras formas para imprimir dados específicos de um dicionários:
print(aluno.items())
print(aluno.keys())
print(aluno.values())