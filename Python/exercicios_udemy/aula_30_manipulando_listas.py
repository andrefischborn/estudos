'''
MANIPULANDO LISTAS
Puxar um item
Modificar um item...

'''
cidades = ['Porto Alegre', 'São Paulo', 'Rio de Janeiro', 'Curitiba', 'Florianópolis', 'Recife']
print(cidades)


#Brincando com algumas manipulações:

cidades.reverse()
print(cidades, 'Inverte a ordem de "Index", começa do ultimo para o primeiro!')

cidades.append('Guaporé')  # Insere o dado no FINAL da lista!
print(cidades, '- Foi adicionado o item "Guaporé" no final da lista!')

cidades.insert(1, 'Santa Cruz') # Podemos inserir um dado em uma posição index escolhida.
print(cidades, '- Foi adicionado o item "Santa Cruz" no "Index 1" da lista!')

cidades.remove('Rio de Janeiro')    # Remove um item da lista, precisa do nome correto.
print(cidades, '- Foi retirado o item Rio de Janeiro da lista!')

cidades.pop(0)  # Remove a posição index, sem precisar digitar o que está nela.
print(cidades, '- Foi retirado o item de "Index 0" da lista!')

cidades.sort()
print(cidades, '- Foi listado de forma alfabética (A a Z) os "Indexes"!')

