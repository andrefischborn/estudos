'''
Usando o REPLACE().

'''
mensagem = 'eu adoro comer comida caseira.'
print(mensagem)

# neste comando vai substituir a palavra "caseira" por "feita em casa" - Lembre que o Python é casesensive.
print(mensagem.replace('caseira', 'feita em casa'))

# podemos substituir as letras da frase por outras:
print(mensagem.replace('a', 'e'))
