'''
    Problema "temperatura"
Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com
duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius (você deve
deduzir a fórmula de Celsius para Fahrenheit):
C = (F - 32) * (5 / 9)
F = C * (9 / 5) + 32

    Exemplo 1:
        Voce vai digitar a temperatura em qual escala (C/F)? F
        Digite a temperatura em Fahrenheit: 75.00
        Temperatura equivalente em Celsius: 23.89
    Exemplo 2:
        Voce vai digitar a temperatura em qual escala (C/F)? C
        Digite a temperatura em Celsius: 28.15
        Temperatura equivalente em Fahrenheit: 82.67
'''
repetir = 's'
while repetir == 's':

    tipo = input(
        'Você vai digitar a temperatura em Celsius ou Fahrenheit? (C/F)? ').upper()
    print()

    def celsius():
        print(f'Você escolheu converter a temperatura de Celsius para Fahrenheit.')
        temperatura = float(input('Digite a temperatura em Celsius: '))
        convertida = float(temperatura * (9 / 5) + 32.0)
        print(f'Temperatura equivalente em Fahrenheit: {convertida:.2f}')


    def fahrenheit():
        print(f'Você escolheu converter a temperatura de Fahrenheit para Celsius.')
        temperatura = float(input('Digite a temperatura em Fahrenheit: '))
        convertida = float((temperatura - 32.0) * (5 / 9))
        print(f'Temperatura equivalente em Celsius: {convertida:.2f}')


    if tipo == 'C':
        celsius()
    elif tipo == 'F':
        fahrenheit()
    else:
        print(f'Digite uma opção válida.')
    repetir = input('Repetir? (S/N): ').lower()