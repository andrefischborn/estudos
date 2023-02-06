'''
For Loop dentro da lista

'''

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# vamos supor que eu queria selecionar apenas as frutas que contenham a letra b
'''
lista = [] # cria uma lista vazia
for item in frutas1:
    if 'b' in item:
        lista.append(item)

print(lista)
'''
# podemos deixar o código mais interativo com o usuário usando um input:

letra = input('Qual letra você quer pesquisar? ')
lista = []
for item in frutas1:
    if letra in item:
        lista.append(item)


print(lista)