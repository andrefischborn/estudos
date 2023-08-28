# Trabalhando com STRINGS
set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

# Unindo duas variaveis
set4 = set1.union(set2)
print(set4)

# O que tem de diferente entre as variaveis:
set5 = set1.difference(set3)
print(set5)

# Qual item tem em comum nas duas variaveis:
set6 = set1.intersection(set2) 
print(set6)

# Lista todos que Não estão duplicados: É contrário do intersection.
set7 = set1.symmetric_difference(set3)
print(set7)

# Existem várias outros operadores muito importantes.
