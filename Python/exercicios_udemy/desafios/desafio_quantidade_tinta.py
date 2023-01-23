'''
                        Desafio com funções:

Criar um programa que calcula a quantidade de tinta necessária para pintar
uma parede. O usuário deverá fornecer as seguintes informações: Rendimento,
altura e largura.
O programa deverá mostrar na tela a mesnagem: "Você necessita de x latas de tinta".
'''

altura = float(input(f'Informe a altura da parede: '))
largura = float(input(f'Informe a largura da parede: '))
rendimento = float(input(f'Informe o rendimento dessa tinta: '))
litros = (altura * largura) / rendimento
galao = 3.6
lata = 18

def calculo():
    print(f'Para essa área de {altura*largura}m² você vai precisar de {litros:.1f} litros dessa tinta por demão.')
    print()
    print(f'Se você optar por comprar Latas de 3.6L, usará {litros/galao:.2f} latas. (Por demão).')
    print(f'Se você optar por comprar Latas de 18L, usará {litros/lata:.2f} latas. (Por demão).')
calculo()


# totalmente desnecessário fazer uma função para esse código, mas foi o professor que pediu.