'''
TRABALHANDO COM VÁRIOS XARGS E NOMEANDO PARAMETROS - IDENTIFICAR OS ARGUMENTOS

exemplo:
Vamos supor que precisamos criar um catalogo para uma agência de carros por MODELO, COR, MOTOR E PLACA.

'''
# esse método funcionaria:

def agencia(*carro):
    return carro


print(agencia('Modelo: Gol', 'Cor: Azul', 'Motor: 1.0', 'Placa: 1256'))
print()

# mas tem coisa melhor
# MÉTODO MELHOR:

def agencia2 (**carros):
    return carros


print(agencia2(Modelo='Gol', Cor='Branco', Motor=1.0, Placa=1234))    
print(agencia2(Modelo='Gol', Cor='Preto', Motor=2.0, Placa=1534))
print(agencia2(Modelo='Onyx', Cor='Vermelho', Motor=1.5, Placa=9221))
print(agencia2(Modelo='Civic', Cor='Cinza', Motor=2.0, Placa=3567))

# É criado um dicionário!
