'''
FILTER FUNCTION
    Muito utilizado com listas
    Aplicar uma função a um Iterable, filtrando os itens. (List, tuple, dic, etc.)
'''
valores = [10, 12, 34, 44, 57]

def abaixo20(x):
    return x > 20


print(list(filter(abaixo20, valores)))  # Empregando o Filter

# Deixando mais enxuto sem precisar da function:
print(list(filter(lambda x: x > 20, valores)))
