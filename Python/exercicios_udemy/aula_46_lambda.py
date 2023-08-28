'''
Lambda Function:
    É uma função (pequena) sem nome
    Pode ter vários argumentos mas somente 1 expressão
    Muito utilizada dentro de outras funções, é como se fosse uma "subfunção"
    Deixa o código mais "Clean"
'''

def somar(x):
    return x + 10


print(somar(2))


# Esse lambda faz a mesma coisa da function acima:
somar = lambda x: x + 10
print(somar(2))
