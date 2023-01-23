'''
            # Problema "idades"
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.

Exemplo:
    Dados da primeira pessoa:
    Nome: Maria Silva
    Idade: 19
    Dados da segunda pessoa:
    Nome: Joao Melo
    Idade 20
    A idade média de Maria Silva e Joao Melo é de 19.5 anos 
'''
pessoa1 = input('Qual o nome da primeira pessoa? ').title()
idade1 = int(input(f'Qual a idade de {pessoa1}? '))
pessoa2 = input('Qual o nome da segunda pessoa? ').title()
idade2 = int(input(f'Qual a idade de {pessoa2}? '))
media = (idade1 + idade2) / 2

print()
print('Dados da primeira pessoa:')
print(f'Nome: {pessoa1}.')
print(f'Idade: {idade1} anos.')
print('Dados da segunda pessoa:')
print(f'Nome: {pessoa2}.')
print(f'Idade: {idade2} anos.')
print(f'A idade média de {pessoa1} e {pessoa2} é de {media:.2f} anos.')
