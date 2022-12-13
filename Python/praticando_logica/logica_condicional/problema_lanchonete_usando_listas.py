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

precos = [0, 5.0, 3.5, 4.8, 8.9, 7.32]
print(f'Código 1 = R$ {precos[1]:.2f}')
print(f'Código 2 = R$ {precos[2]:.2f}')
print(f'Código 3 = R$ {precos[3]:.2f}')
print(f'Código 4 = R$ {precos[4]:.2f}')
print(f'Código 5 = R$ {precos[5]:.2f}')

codigo = int(input('Qual o código do produto desejado? '))

if (codigo > 5) or (codigo == 0):
    print('Código Invalido.')

else:
    quantidade = int(input('Qual a quantidade comprada? '))

total = quantidade * precos[codigo]

print(f'Código do produto comprado: {codigo}')
print(f'Quantidade comprada: {quantidade}')
print(f'Valor a pagar: R$ {total:.2f}')
