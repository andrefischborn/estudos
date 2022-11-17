'''
TRABALHANDO COM VÁRIOS XARGS E NOMEANDO PARAMETROS - IDENTIFICAR OS ARGUMENTOS

exemplo:
Vamos supor que precisamos criar um catalogo para uma agência de carros por MODELO, COR, MOTOR E PLACA.

'''

def agencia(*carro):
    return carro


print(agencia('Gol','Azul', 1.0))   # esse método funcionaria, mas tem coisa melhor:



# METODO MELHOR:

def agencia2 (**carros):
    return carros


print(agencia2(Marca='Gol', Cor='Branco', Motor=1.0, Placa=123))    # É criado um dicionário!
