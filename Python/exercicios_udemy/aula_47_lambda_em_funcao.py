'''
Lambda Function:
    É uma função (pequena) sem nome
    Pode ter vários argumentos mas somente 1 expressão
    Muito utilizada dentro de outras funções, é como se fosse uma "subfunção"
    Deixa o código mais "Clean"
'''

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) *4


print(somar(2))