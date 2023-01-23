'''
            Comando: "WHILE" - QUER DIZER ENQUANTO.
É uma estrutura de controle que REPETE um bloco de comandos ENQUANTO uma condição for verdadeira.
Usamos quando NÃO sabemos previamente a quantidade de repetições que será realizada.
'''
###########################################################################################
'''
Exercício:
Fazer um programa que lê números inteiros até que um zero seja lido.
Ao final mostrar a soma dos números lidos.
    
    Primeiro número: 5
    Outro número: 2
    Outro número: 4
    Outro número: 0
    SOMA = 11
'''
num = int(input('Digite o primeiro número: '))
soma = 0    # A variável "soma" precisa existir antes do WHILE começar os loops. Precisa de um valor inicial.

while num != 0:
    soma = soma + num   # aqui ele acumulando a soma na variavel.
    print(f'Número: {num}')
    num = int(input('Digite outro número: '))
print(f'SOMA: {soma}')
