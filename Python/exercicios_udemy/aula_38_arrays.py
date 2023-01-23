from array import array
'''
                            Trabalhando com ARRAYs (MATRIZES)
Muito confundido com Lista e Tuples.
Usamos Array quando a lista for MUITO grande e estamos temo problemas de performance. Ela tem as mesmas características, mutável...
Arrays não são disponíveis default no python. Precisamos importar um módulo! 
Usamos: 
            from array import array
'''
letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])   # o 'u' é para dizer que a array está em UNICODE CHARACTER. Deve ser minúsculo.
                                            # 'u' = Strings, 'i' = Interger. 'f' = Float - Existe outros, ver no google.
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)
