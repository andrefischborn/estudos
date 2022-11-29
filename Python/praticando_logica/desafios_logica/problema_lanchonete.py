'''
            Problema "lanchonete" (adaptado de URI 1038)
Uma lanchonete possui vários produtos. Cada produto possui um código
e um preço. Você deve fazer um programa para ler o código e a
quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais, conforme
tabela de produtos ao lado.
                                            Código do produto   Preço do produto
                                                1                   R$ 5.00
                                                2                   R$ 3.50
                                                3                   R$ 4.80
                                                4                   R$ 8.90
                                                5                   R$ 7.32
    Exemplo 1:
        Codigo do produto comprado: 1
        Quantidade comprada: 3
        Valor a pagar: R$ 15.00
    Exemplo 2:
        Codigo do produto comprado: 4
        Quantidade comprada: 2
        Valor a pagar: R$ 17.80 
'''
codigo = int(input('Qual o código do produto? '))

if codigo > 5:
    print('Código Invalido.')
else:
    quantidade = int(input('Qual a quantidade comprada? '))

if codigo == 1:
    preco = 5.0
if codigo == 2:
    preco = 3.5
if codigo == 3:
    preco = 4.8
if codigo == 4:
    preco = 8.9
if codigo == 5:
    preco = 7.32

total = quantidade * preco
print(f'Código do produto comprado: {codigo}')
print(f'Quantidade comprada: {quantidade}')
print(f'Valor a pagar: R$ %.2f' % (total))