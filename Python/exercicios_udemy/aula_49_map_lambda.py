# Essa é uma forma enxuta de fazer, trocamos o DEF por Lambda:

lista1 = [1, 2, 3, 4 ]

lista2 = map(lambda x: x * 2, lista1)

print(lista1)
print(list(lista2)) # Se não colocar o "list", a impressão será um OBJETO:
print(lista2)


# Aqui colocamos tudo em apenas duas linhas de código usando o lambda direto na impressão:

lista1 = [1, 2, 3, 4 ]
print(list(map(lambda x: x * 2, lista1))) 