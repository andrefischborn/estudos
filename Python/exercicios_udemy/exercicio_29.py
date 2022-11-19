'''
TRABALHANDO COM LISTAS
Listas servem para guardar informações em váriaveis e manter a ordem sequencial na qual foi escrita.

para não precisa fazer:

    cidade1 = 'Porto Alegre'
    cidade2 = 'São Paulo'
    cidade3 = 'Rio de Janeiro'

usamos:
    cidades[] # Dentro do colchete vai o nome das cidades separadas por vírgula.
'''

cidades = ['Porto Alegre', 'São Paulo', 'Rio de Janeiro', 'Curitiba', 'Florianópolis', 'Recife']
print(cidades)

# Podemos Manipular itens na lista que serão impressos a partir do comando de impressão:

cidades[0] = 'Taquara' # 0 é o primeiro item da lista index. Era Porto Alegre e será substituído por Taquara.
print(cidades)

cidades[4] = 'São Francisco' # Vai trocar Florianópolis por São Francisco. Porto Alegre vai continuar trocada por Taquara.
print(cidades)
