'''
                # Problema "troco"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.

    Exemplo 1:
        Preço unitário do produto: 8.00
        Quantidade comprada: 2
        Dinheiro recebido: 20.00
        TROCO = 4.00
    Exemplo 2:
        Preço unitário do produto: 30.00
        Quantidade comprada: 3
        Dinheiro recebido: 100.00
        TROCO = 10.00 
'''
produto = input('Qual produto? ')
preco = float(input('Qual o preço do produto? '))
quantidade = int(input('Quantidade a ser comprada? '))
dinheiro_recebido = float(input('Quanto de dinheiro foi dado? '))
troco = (dinheiro_recebido - (preco * quantidade))


print(f'Foi comprado o produto: {produto}.')
print(f'Quantidade comprada: {quantidade}')
print(f'Preço unitário do produto: {preco:.2f}')
print(f'Dinheiro recebido: {dinheiro_recebido:.2f}')
print(f'TROCO: {troco:.2f}')