'''
Problema "experiencias" (adaptado de URI 1094)
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
percentual deve ser apresentado com dois dígitos após o ponto.
    Exemplo:
        Quantos casos de teste serao digitados? 10
        Quantidade de cobaias: 10
        Tipo de cobaia: C
        Quantidade de cobaias: 6
        Tipo de cobaia: R
        Quantidade de cobaias: 15
        Tipo de cobaia: S
        Quantidade de cobaias: 5
        Tipo de cobaia: C
        Quantidade de cobaias: 14
        Tipo de cobaia: R
        Quantidade de cobaias: 9
        Tipo de cobaia: C
        Quantidade de cobaias: 6
        Tipo de cobaia: R
        Quantidade de cobaias: 8
        Tipo de cobaia: S
        Quantidade de cobaias: 5
        Tipo de cobaia: C
        Quantidade de cobaias: 14
        Tipo de cobaia: R
    RELATORIO FINAL:
    Total: 92 cobaias
    Total de coelhos: 29
    Total de ratos: 40
    Total de sapos: 23
    Percentual de coelhos: 31.52
    Percentual de ratos: 43.48
    Percentual de sapos: 25.00 

'''
s = 0
r = 0
c = 0
total = s + r + c

experimentos = int(input(f'Quantos casos de teste serão digitados? '))

for i in range(0, experimentos):
    quantidade = int(input(f'Quantidade de Cobaias: '))
    tipo = str(input(f'Tipo de cobaia: ')).lower()
    
    if tipo == 's':
        s = s + quantidade
    elif tipo == 'r':
        r = r + quantidade
    elif tipo == 'c':
        c = c + quantidade
    else:
        print(f'Tipo Inválido')
        quantidade = int(input(f'Quantidade de Cobaias: '))
        tipo = str(input(f'Tipo de cobaia: ')).lower()

total = s + r + c
pc = (c / total) * 100
ps = (s / total) * 100
pr = (r / total) * 100

print(f'RELATÓRIO FINAL:')
print(f'Total: {total} cobaias.')
print(f'Total de Coelhos: {c}.')
print(f'Total de Ratos: {r}.')
print(f'Total de Sapos: {s}.')
print(f'Percentual de Coelhos: {pc:.2f}%.')
print(f'Percentual de Ratos: {pr:.2f}%.')
print(f'Percentual de Sapo: {ps:.2f}%.')
