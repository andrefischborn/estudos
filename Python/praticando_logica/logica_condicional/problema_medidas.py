'''
            # Problema "medidas"
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C

    Exemplo 1:
            Digite a medida A: 4.0
            Digite a medida B: 3.5
            Digite a medida C: 5.2
            AREA DO QUADRADO = 16.0000
            AREA DO TRIANGULO = 7.0000
            AREA DO TRAPEZIO = 19.5000
    Exemplo 2:
            Digite a medida A: 7.13
            Digite a medida B: 8.05
            Digite a medida C: 11.912
            AREA DO QUADRADO = 50.8369
            AREA DO TRIANGULO = 28.6983
            AREA DO TRAPEZIO = 90.4121 
'''

medida_a = float(input('Qual a medida do lado "A"? '))
medida_b = float(input('Qual a medida do lado "B"? '))
medida_c = float(input('Qual a medida do lado "C"? '))

def quadrado():
        area = medida_a * medida_a
        print(f'AREA DO QUADRADO = %.4f' % (area))

        
def triangulo():
        area = medida_a * medida_b / 2
        print(f'AREA DO TRIANGULO = %.4f' % (area))


def trapezio():
        area = 0.5 * medida_c * (medida_a + medida_b)
        print(f'AREA DO TRAPEZIO = %.4f' % (area))


quadrado()
triangulo()
trapezio()