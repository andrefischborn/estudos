'''
                USANDO Variáveis dentro de FUNCTION.
Elas não pertencem ao código global, dessa forma podemos repetir nomes de variáveis sem dar conflito.
'''
#FUNCTION 1
def somar_dois_numeros():
    numero1 = 10
    numero2 = 30
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros()

''' Se colocar:

print(resultado)

Fora da function, vai dar erro. As variáveis não estão dentro do código global.

Agora, estamos usando os mesmos nomes de variáveis com valores diferentes:
'''

#CODIGO GLOBAL:
numero1 = 30
numero2 = 50
resultado = numero1 + numero2
print(resultado)

#vai ser impressos as duas sem dar conflito!

#Vamos criar outra FUNCION, igualzinha a primeira, só que com nome diferente:

#FUNCTION 2
def somar_dois_numeros2():
    numero1 = 120
    numero2 = 320
    resultado = numero1 + numero2
    print(resultado)


somar_dois_numeros2()

# Olha só, usavamos as mesmas variáveis 3 vezes no mesmo código e não tivemos conflito nenhum!

#repetindo as impressões para ficar claro e mostrar a evitação do "DRY":
print('Tudo bonito:')
somar_dois_numeros()
somar_dois_numeros2()
print(resultado)
