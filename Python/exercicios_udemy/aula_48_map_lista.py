'''
MAP FUNCTION
    Muito utilizado em listas
    Aplicar uma função a um Iterable, por item, (Lista, tuple, dic, etc)

'''

lista1 = [1, 2, 3, 4 ]

def multi(x):
    return x * 2


lista2 = map(multi, lista1)

print(lista1)
print(list(lista2)) # Se não colocar o "list", a impressão será um OBJETO:
print(lista2)