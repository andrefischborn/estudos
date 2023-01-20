'''
COMANDO WHILE LOOP (ENQUANTO)
Tem um funcionamento um pouco diferente do "For Loop" e diferente do IF / ELSE
O while fica girando até a condição acabar. É diferente do IF / ELSE, que só executa a condição uma vez só, ou é, ou não é.

Exercicio: Criar uma promoção progressiva de diminuir o preço em 5 reais por dia até chegar em um valor minímo.
'''

valor = 50
dia = 0

while valor > 20:
    dia +=1 # Aqui vai acrescentar um dia por loop.
    print(f'Dia: {dia} - O valor de hoje é R${valor}!') 
    print()
    valor -= 5 # Aqui baixa 5 reais por loop.

'''
No For Loop você diz quantos giros você quer. Quero 3... Quero 50... É colocado um limite.
No while Loop é enquanto a condição existir. Pode se tornar infinito. Também é funcional quando não sabemos a quantidade que vai ser.

For Loop = Faça 50 flexões por 50 dias.
For While = Faça flexões até cansar, por 50 dias ou até morrer.

'''