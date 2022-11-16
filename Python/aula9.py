'''
                Declarações Condicionadas

    Verificações em variáveis - IF / ELSE / ELIF

'''

# juntando conhecimento da aula6.
velocidade = input('Qual a sua velocidade? ')

# precisamos definir o tipo da variável. Sera um número inteiro para poder ter a mesma classe de comparação (número)

velocidade = int(velocidade)  # int é número inteiro.

if velocidade > 100:
    print('Velocidade excedida!')

elif velocidade < 60:
    print('Velocidade baixa demais!')

else:
    print('Velocidade dentro do permitido.')
