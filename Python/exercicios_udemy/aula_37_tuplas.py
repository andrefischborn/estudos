# Entendo a diferença entre TUPLE e LISTA:

# Tuple
#   Serve para armazenar mais de uma informação em variáveis.
#   Mantém a sequência dos dados de uma variável
#   Não podem ser alteradas. IMMUTABLE. - Maior diferença!

cores_list = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
cores_tuple = ('Amarelo', 'Verde', 'Azul', 'Vermelho')  # A Tuple usa PARENTESES() ao invés de colchetes[]!

# o comando TYPE faz o python dizer o tipo de classe da variável.
print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2 # Também funcionará com a tuple: duas_listas = cores_tuple * 2
print(duas_listas)

# Se tentar adicionar itens na tuple, vai dar erro!
# cores_tuple.append('Roxo')

# Com a lista funciona normalmente:
cores_list.append('Roxo')

print(f'Cores na LIST: {cores_list}')
print(f'Cores na TUPLE: {cores_tuple}')

# Uma tuple gasta menos memória que a lista, sendo assim, o código é mais rápido.
# Portanto sempre que for trabalhar com dados FIXOS, IMUTÁVEIS, devemos preferir usar as TUPLES!
