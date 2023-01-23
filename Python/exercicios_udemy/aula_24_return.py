'''
PRINT E RETURN
Quando algo é impresso, este dado não é armezanado,

'''

def cliente1(nome):
    print(f'Olá {nome}!') # Imprime normalmente e descarta.


cliente1('Maria')   # Aqui vai funcionar
#O valor "Maria" é simplesmente impresso e pronto, não fica salvo para o próximo comando.

print(cliente1('Maria'))    # Aqui vai apresentar "Erro" - "NONE" porque já foi descartado antes.

 
print() # Só para separar a linha.


def cliente2(nome):
    return(f'Olá {nome}')


cliente2('Pedro')   # Esse não vai imprimir porque está com return, ele está armazenando o dado.
print(cliente2('Pedro'))    # Esse comando faz imprimir o "return" (dado armazenado).

# VAMOS ENXUGAR o código acima no próximo exercicio(25).