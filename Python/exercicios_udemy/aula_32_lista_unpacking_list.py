'''
#Unpacking Lists
    Armazenar mais de uma infomação em variáveis
    Manter a sequência dos dados em uma variável
'''


''' Forma menos produtiva de fazer esse código:

produtos = ['arroz', 'feijão', 'laranja', 'banana']
# index        0         1         2         3 
item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]

print(item1)
print(item2)
print(item3)
print(item4)
'''

# Melhor forma:

'''
produtos = ['arroz', 'feijão', 'laranja', 'banana']
item1, item2, item3, item4 = produtos

print(item1)
print(item2)
print(item3)
print(item4)

'''
# caso não queira imprimir todas e não dar erro, usamos *algumnome

produtos = ['tomate', 'pepino', 'lentilha', 'maça', 'repolho', 'abacate']
item1, item2, *outros, item5 = produtos

print(item1)
print(item2)
print(outros)

# OU fazendo um loop:

for x in produtos:
    print(x)