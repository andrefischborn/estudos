'''
CONCATENANDO LISTAS

'''
numeros = [2,3,4,5]
final = numeros * 2 # A lista se repetirá 2 vezes
print(final)


letras = ['a', 'b', 'c', 'd', 'e']
final2 = (numeros + letras)
print(final2)


# Usando uma forma mais enxuta
numeros.extend(letras) # esse comando faz a mesma coisa do grupo acima, porém sem ter que criar uma nova variavel "final2"
print(numeros)
print()


# Lista dentro de lista - MATRIZ
# Aqui vemos: ["Index0"] com [Index0 e Index1] e ["Index1"]com [Index0 e Index1]:
#index:          0                 1
itens = [['Banana','Laranja'],['Cebola','Batata']] 
# index      0       1          0       1

print(itens)    # Aqui imprime tudo em linha.
print(itens[0]) # Aqui imprime a lista "Index0"
print(itens[1]) # Aqui imprime a lista "Index1"

print(itens[0][0])  # Aqui imprime um item da lista que está dentro da outra lista. "Index0 da Index0".