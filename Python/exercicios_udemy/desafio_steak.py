'''
                Desafio com condições:

Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura.

Temperaturas:
120F ou 49C - Rare (Selada)
130F ou 55C - Medium Rare (Ao ponto para o mal passado.)
140F ou 60C - Medium (Ao ponto)
150F ou 66C - Medium Well (Ao ponto para o bem passado)
160F ou 72C - Well done (Bem passado)
'''

temperatura = float(input(f'Informe a temperatura do steak em Celsius: '))
convertida = float(temperatura * (9 / 5) + 32.0)
print(f'Temperatura equivalente em Fahrenheit: {convertida:.2f}')

if convertida < 120:
    print(f'Seu Steak precisa cozinhar mais.')
elif convertida >= 120 and convertida < 130:
    print(f'Seu Steak está Selado.')
elif convertida in range(130, 140):     # outra forma de fazer 
    print(f'Seu Steak está ao ponto para o mal passado.')
elif convertida >= 140 and convertida < 150:
    print(f'Seu Steak está ao ponto.')
elif convertida >= 150 and convertida < 160:
    print(f'Seu Steak está ao ponto para o bem passado.')
elif convertida >= 160 and convertida < 200:
    print(f'Seu Steak está bem passado.')
elif convertida >= 200:
    print(f'Seu Steak está muito passado.')