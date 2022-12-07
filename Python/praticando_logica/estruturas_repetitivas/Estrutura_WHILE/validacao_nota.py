'''
        Problema "validacao_de_nota" (adaptado de URI 1117)
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a
média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao
intervalo [0 - 10]). Cada nota deve ser validada separadamente.
    Exemplo 1:
        Digite a primeira nota: 3.5
        Digite a segunda nota: 10.0
        MEDIA = 6.75
    Exemplo 2:
        Digite a primeira nota: -3.5
        Valor invalido! Tente novamente: 3.5
        Digite a segunda nota: 11.0
        Valor invalido! Tente novamente: 10.5
        Valor invalido! Tente novamente: 10.0
        MEDIA = 6.75 
'''
nota1 = float(input('Digite a primeira nota: '))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input('Valor inválido! (Deve ser: 0 - 10). Tente novamente: '))

nota2 = float(input('Digite a segunda nota: '))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Valor inválido! (Deve ser: 0 - 10). Tente novamente: '))

media = (nota1 + nota2) /2

print(f'MÉDIA: %.2f' % (media))
