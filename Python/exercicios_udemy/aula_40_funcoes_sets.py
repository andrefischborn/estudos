'''
Set Listas
Sim

'''

list1 = set([1, 2, 3, 4, 5])    # Forma mais longa de criar um SET
s1 = {1, 2, 3, 4, 5}    # Forma enxuta e inteligente de criar um SET - Não usar essa forma para criar SET VAZIO!

# O resultado de impressão será o mesmo:
print(list1)
print(s1)

# Comando para descobrir o TIPO da variável e mostrar que ambas são "Sets":
print(type(list1))
print(type(s1))

#Podemos adicionar itens no SET:
s1.add(8) # Comando ADD, para adicionar.
s1.add(3) # Se o dado já estiver listado, ele não sera impresso novamente.
print(s1)

# Também podemos usar este comando: Ele Também não duplica dados repetidos.
s1.update([2, 9, 7, 8, 10, 9, 6]) # Não precisa colocar em ordem. Ele mesmo coloca.
print(s1)