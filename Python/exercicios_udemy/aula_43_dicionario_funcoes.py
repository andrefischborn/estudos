'''
Update

'''
# Criando o dicionário:
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': 'true'} # um dicionário é como uma lista, ele é mutavel.

# Comando UPDATE Adiciona ou muda um dado da lista:
aluno.update({'endereco': 'Rua A'}) #
aluno.update({'nome': 'Pedro ='})
print(aluno)


# Trabalhando com GET:
print(aluno.get('idade'))   # Podemos imprimir apenas um dado específico.
print(aluno.get('email'))   # Caso coloque um item que não existe, ele reportará como NONE.
print(aluno.get('email', 'NAO EXISTE'))   # Também podemos manipular o que irá aparecer


# Comando para deletar um item da lista:
del aluno['nome'] # O nome não irá aparecer porque será deletado da lista.
print(aluno)