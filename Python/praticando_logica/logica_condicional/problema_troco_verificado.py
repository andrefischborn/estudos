'''
        Problema "troco_verificado"
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante conforme exemplo.
    Exemplo 1:
        Preço unitário do produto: 8.00
        Quantidade comprada: 2
        Dinheiro recebido: 20.00
        TROCO = 4.00 
    Exemplo 2:
        Preço unitário do produto: 30.00
        Quantidade comprada: 3
        Dinheiro recebido: 70.00
        DINHEIRO INSUFICIENTE. FALTAM 20.00 REAIS 
'''
preco_unitario = float(input(f'Qual o preço unitário do produto? '))
quantidade_comprada = int(input(f'Quantos produtos foram comprados? '))
dinheiro_pago = float(input(f'Quanto de dinheiro foi dado pelo cliente? '))
valor_total = preco_unitario * quantidade_comprada
troco = dinheiro_pago - valor_total
falta = valor_total - dinheiro_pago

if dinheiro_pago < valor_total:
    print(f'DINHEIRO INSUFICIENTE. FALTAM R$ {falta:.2f} REAIS.')
else:
    print(f'TROCO: R$ {troco:.2f} REAIS.')
