# exercicio usando WHILE. Cadastrar um produto que será publicado com comissão de 10% se o preço for maior que 20.

produto = input('Qual produto você quer cadastrar? ')
preco = float(input('Qual o preço do produto? '))
preco_final = (preco * 0.10) + preco
comissao = preco_final - preco
comissao = float(comissao)
while preco >= 20:
    print(f'Seu produto é: {produto}')
    print(f'O produto deve ser vendido por R$:{preco_final}. Sua comissão será de R$:{comissao}.')
    break
else:
    print(f'Seu produto deve ser vendido por R$:{preco}. Você não terá comissão.')
