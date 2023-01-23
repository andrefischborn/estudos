import math
'''
            # Problema "retangulo"
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos. 

'''
b = float(input('Qual o tamanho da base? ' ))
h = float(input('Qual o tamanho da altura? ' ))

area = b * h
perimetro = 2 * (b+h)
diagonal = math.sqrt(b ** 2 + h ** 2)

print(f'O valor da area deste retângulo é de: {area:.4f}')
print(f'O valor do perimetro deste retângulo é de: {perimetro:.4f}')
print(f'O valor da diagonal deste retângulo é de: {diagonal:.4f}')
