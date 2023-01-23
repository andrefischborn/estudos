# Enxugando o exercicio 24:
def cliente1(nome):
    print(f'Olá {nome}!')   # Imprime normalmente e descarta.


def cliente2(nome):
    return(f'Olá {nome}')


x = cliente1('Maria')
y = cliente2('Pedro')

print(x)    # Vai dar NONE porque não tem nada armazenado.
print(y)    # Esse dado é o que está armazenado no RETURN.