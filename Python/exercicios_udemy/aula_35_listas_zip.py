# Agregando duas listas com o comando ZIP

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

# brincando com o comando list:
# ele transforma uma string em uma "lista", divide cada letra em uma index.
var = list('Palavra')
print(var)
print(f'O item que se encontrar na INDEX5 é a letra: {var[5]}') # podemos pedir para imprimir um item indexado na própria palavra.
print()

#Aqui o index de cada lista forma um par. O index 0 fica do lado do index 0 da outra lista, e assim por diante.
duas_listas = zip(cores, valores)
print(list(duas_listas))
print()

# O comando extend ele junta as listas, mas ele não deixa lado a lado os indexes.
cores.extend(valores)
print(cores)
