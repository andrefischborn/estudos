                                # DESAFIO COM SET
'''
Criar um programa que fera 3 listas de acordo com a necessidade logo abaixo:
lista 1 = Funcionários que tem carro e trabalham a noite;
lista 2 = Funcionários que tem carro e trabalham de dia;
lista 3 = Funcionários que não tem carro.

Nome dos funcionarios = Ana, Marcos, Alice, Pedro, Sophia, Bruno, Melissa
Trabalham de dia =  Ana, Marcos, Alice, Melissa
Trabalham a noite = Pedro, Sophia, Bruno
Tem Carro = Marcos, Alice, Bruno, Melissa
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#                               Modo longo e improdutivo, porém funciona:

lf = set(funcionarios)
ld = set(turno_dia)
ln = set(turno_noite)
lc = set(tem_carro)

print(f'Funcionários que tem carro e trabalham a noite: {lc & ln}') 
print(f'Funcionários que tem carro e trabalham de dia: {lc & ld}')
print(f'Funcionários que não tem carro: {lf - lc}')
print()

#                               Modo enxuto e produtivo:

#lista 1
lista1 = set(tem_carro).intersection(turno_noite)
print(f'Funcionários que tem carro e trabalham a noite:: {lista1}')

#lista 2
lista2 = set(tem_carro).intersection(turno_dia)
print(f'Funcionários que tem carro e trabalham de dia: {lista2}')

#lista 3
lista3 = set(funcionarios).difference(tem_carro)
print(f'Funcionários que não tem carro: {lista3}')
