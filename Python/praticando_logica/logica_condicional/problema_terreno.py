'''
                # Problema "terreno"
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais, conforme exemplo.

# Exemplo 1:
Digite a largura do terreno: 10.0
Digite o comprimento do terreno: 30.0
Digite o valor do metro quadrado: 200.00
Area do terreno = 300.00
Preco do terreno = 60000.00 

# Exemplo 2:

Digite a largura do terreno: 12.0
Digite o comprimento do terrano: 20.0
Digite o valor do metro quadrado: 150.00
Area do terreno = 240.00
Preco do terreno = 36000.00 

'''

largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terreno? '))
valor_metro = float(input('Qual o valor do metro quadrado? '))

area = (largura * comprimento)
preco_terreno = (area * valor_metro)

print(f'A area do terreno é de: {area:.2f}')
print(f'O valor do terreno é R$ {preco_terreno:.2f}')