'''
Agora vamos melhorar nossas Functions, vamos usar PARAMETROS para deixar o código mais enxuto.

'''
# FUNCTION NORMAL:
def boas_vindas_marcos():
    print('Olá Marcos!')


def boas_vindas_andre():
    print('Olá André!')


def boas_vindas_maria():
    print('Olá Maria!')


boas_vindas_marcos()
boas_vindas_andre()
boas_vindas_maria()


# USANDO AGORA OS PARAMETROS:

def boas_vindas(nome):
    print(f'Olá {nome}.')


boas_vindas('Nome da pessoa.')

'''
O PARAMETRO PODE TER DOIS TIPOS DE VALORES
DEFAULT - Aquele que você DEFINE o valor do parametro
NON-DEFAULT - Aquele que você NÃO DEFINE o valor do parametro.
'''
