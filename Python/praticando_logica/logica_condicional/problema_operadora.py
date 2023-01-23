'''
    Problema "operadora"
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.
    Exemplo 1:
        Digite a quantidade de minutos: 22
        Valor a pagar: R$ 50.00
    Exemplo 2:
        Digite a quantidade de minutos: 103
        Valor a pagar: R$ 56.00 
'''
consumo = int(input(f'Quantos minutos foram utilizados? '))
valor_extra = 2.00 * (consumo - 100)
minutos_extra = consumo - 100
valor_total = valor_extra + 50
print()
if consumo <= 100:
    print(f'Seu consumo de dados não foi excedido.')
    print(
        f'Total de minutos utilizados: {consumo}min. Sua conta atual é de: 50.00 reais')
else:
    print(
        f'A sua franquia excedeu os minutos contratatos em: {minutos_extra} min. Você pagará extra: {valor_extra:.2f} reais.')
    print()
    print(
        f'Total de minutos utilizados: {consumo} min. Sua conta atual é de: R$ {valor_total:.2f} reais.')
