'''
        Problema "combustivel" (adaptado de URI 1134)
Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido codificado da seguinte forma:
        1.Álcool 2.Gasolina 3.Diesel 4.Fim. 
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido).
O programa será encerrado quando o código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
como as quantidades de cada combustível.
    Exemplo:
        Informe um codigo (1, 2, 3) ou 4 para parar: 8
        Informe um codigo (1, 2, 3) ou 4 para parar: 1
        Informe um codigo (1, 2, 3) ou 4 para parar: 7
        Informe um codigo (1, 2, 3) ou 4 para parar: 2
        Informe um codigo (1, 2, 3) ou 4 para parar: 2
        Informe um codigo (1, 2, 3) ou 4 para parar: 4
        MUITO OBRIGADO
        Alcool: 1
        Gasolina: 2
        Diesel: 0 
'''
print(f'Informe um código: <1>Álcool  <2>Gasolina  <3>Diesel  <4>Fim.')
codigo = int(input())

alcool = 0
gasolina = 0
diesel = 0


while codigo != 4:
    if codigo == 1:
        alcool = alcool + 1
    elif codigo == 2:
        gasolina = gasolina + 1
    elif codigo == 3:
        diesel = diesel + 1
    print(f'Informe um código: <1>Álcool  <2>Gasolina  <3>Diesel  <4>Fim.:')
    codigo = int(input())
    
print(f'Muito Obrigado')   
print(f'ALCOOL: {alcool}')
print(f'GASOLINA: {gasolina}')
print(f'DIESEL: {diesel}')
